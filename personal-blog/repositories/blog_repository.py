from bson import ObjectId
from datetime import datetime
from content_gpt_backend.repositories.blog_interface_repository import IBlogRepository
from content_gpt_backend.entity_manager.manager import entity_manager
from content_gpt_backend.dtos.blog_dto import blog_input , blog
from content_gpt_backend.dtos.custom_response import BLOG_IN_PROGRESS
from content_gpt_backend.celery_worker import generate_blog
from content_gpt_backend.utils.utilities import modify_blog_count

class BlogRepository(IBlogRepository):
    def __init__(self):
        self.blog_collection = entity_manager.get_collection("blogs")
    
    def add_blog_request_to_celery(self, blog_request:blog_input , user_info:dict):
        
        blog_object = blog(**{
            "topic": blog_request.topic,
            "instructions": blog_request.instructions,
            "content": "",
            "user_email": user_info['email'],
            "created_at": datetime.now()
        })
        blog_doc = self.blog_collection.insert_one(blog_object.dict())
        blog_id = str(blog_doc.inserted_id)
        modify_blog_count(operation="add",email=user_info["email"])
        generate_blog.delay(blog_id , blog_request.topic, blog_request.instructions,  user_info["email"])
        return BLOG_IN_PROGRESS
    
    def get_blog(self,blog_id:str):
        blog_data = self.blog_collection.find_one({"_id":ObjectId(blog_id)})
        blog_data["_id"] = str(blog_data["_id"])
        return blog_data
    