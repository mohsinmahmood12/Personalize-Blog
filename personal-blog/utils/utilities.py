from content_gpt_backend.entity_manager.manager import entity_manager
from entity_manager.logger import logger

def modify_blog_count(operation:str,email:str,user_id:str=None):
    try:
        user_collection = entity_manager.get_collection("users")
        query = {"email": email}

        if operation == "add":
            update = {"$inc": {"blogs_count": 1}}
        else:
            update = {"$inc": {"blogs_count": -1}}
        
        user_collection.update_one(query,update)
        logger.info("User's blog count is updated")

    except Exception as e:
        logger.error(f"Error in updating user's blog count: {e}")

