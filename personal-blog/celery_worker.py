from celery import Celery
from celery.signals import task_success
import requests
from bson import ObjectId
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from dotenv import load_dotenv
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from content_gpt_backend.entity_manager.manager import entity_manager
from content_gpt_backend.entity_manager.logger import logger
from content_gpt_backend.utils.utilities import modify_blog_count
from content_gpt_backend.dtos.blog_dto import blog
from content_gpt_backend.websocket_manager import socket_manager
import asyncio
import time
load_dotenv()

print("REDDIS SERVER URL : ",   entity_manager.reddis_conf)
celery = Celery(__name__)
celery.conf.broker_url = entity_manager.reddis_conf
celery.conf.result_backend = entity_manager.reddis_conf
celery.conf.broker_connection_retry_on_startup =  True
celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)

logger.info("celery worker connected")



llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.6 , api_key=entity_manager.open_ai_key ,max_tokens=3000) 
search = TavilySearchResults(max_results=20)
tools = [search]

# include long paragraphs, titles , categories , bullets , quotes . .. 

system_prompt = """
You are a world-class blog writer specialized in generating content on health and wellness, personal development,
longevity, fitness, diet and exercise, relationships, and workplace intelligence. Your blogs integrate relevant studies
and statistics from credible sources accessed via the Tavily search tool. You adapt your writing style from informative
and technical to engaging and conversational, depending on the topic. Ensure to cite sources accurately and integrate
study data authentically into the blog posts.
"""


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("assistant", "{agent_scratchpad}"),
        ("user", "{input}"),
    ]
)

def create_agent_executor(user_input: str, instructions: str | None = None):
    agent = create_openai_functions_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    formatted_input = (
        'User Query: "{}"'.format(user_input.strip())
        + (
            '\n\nInstructions for Content Generation:\n- Please adhere to the following guidelines: "{}"'.format(
                instructions.strip()
            )
            if instructions
            else ""
        )
    ).strip()

    response = agent_executor.invoke({"input": formatted_input})

    return response["output"]


async def publish_socket_message(message,user_id):
    await socket_manager.send_personal_message(message, user_id)


@celery.task
def generate_blog(blog_id:str , topic:str , instructions:str ,  user_email:str):
    
    try:
        # time.sleep(3)
        # response = "This is dummy blog for "+user_email
        response = create_agent_executor(topic, instructions)
        blog_collection = entity_manager.get_collection("blogs")
        filter = {'_id': ObjectId(blog_id) }
        update = {'$set': {'content': response , "status":"completed"}}
        blog_collection.update_one(filter,update)
        logger.info("Blog has been stored for user successfully")
        

    except Exception as e:
        logger.error(e)
        filter = {'_id': ObjectId(blog_id) }
        update = {'$set': {'content': response , "status":"failed"}}
        blog_collection.update_one(filter,update)
        modify_blog_count(operation="subtract",email=user_email)
        logger.error(f"Error while generating blog : {e}")
        
    
    finally:
        logger.info("Socket Called")
        requests.post("http://localhost:8000/notify", json={"message":"blog updated" , "user_id": f"{user_email}"})


# @task_success.connect
# def task_success_handler(sender=None, result=None, **kwargs):
#     logger.info(sender.name)
    # Notify FastAPI server
    #

    

