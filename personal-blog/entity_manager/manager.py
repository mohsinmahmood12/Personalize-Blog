import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv
from entity_manager.logger import logger
# Load environment variables from the .env file
load_dotenv()

# Get MongoDB credentials from environment variables


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = os.environ.get("DATABASE")
REDDIS = os.environ.get('REDDIS')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
# Create the entity manager
class EntityManager:
    def __init__(self):

        try:
            self.mongo_client = MongoClient(MONGO_URI,maxPoolSize=15,serverSelectionTimeoutMS=5000)
            self.mongo_client.list_database_names()
            self.db_instance = self.mongo_client[DATABASE]
            self.reddis_conf = REDDIS
            self.open_ai_key = OPENAI_API_KEY
            self.tavily_api_key = TAVILY_API_KEY
            logger.info("Database connected")
        except Exception as e:
            logger.error("Failed to connect to database")
            sys.exit(1)

    def get_collection(self, collection_name):
        return self.db_instance[collection_name]

# Instantiate the entity manager
entity_manager = EntityManager()