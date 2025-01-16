from fastapi import HTTPException, Depends, Header
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from content_gpt_backend.services.blog_service import BlogService
from content_gpt_backend.dtos.blog_dto import blog_input
from content_gpt_backend.middlewares.auth import authentication
from content_gpt_backend.entity_manager.logger import logger


blog_controller_router = InferringRouter()

@cbv(blog_controller_router)
class BlogController:
    def __init__(self): 
        self.blogService = BlogService()
    
    @blog_controller_router.post("/generate_blog")
    def process_incoming_blog_generation_request(self, blog_request: blog_input , user_info:str=Depends(authentication)):
        try:
            response = self.blogService.process_blog_request(blog_request,user_info)
            return response
        except Exception as e:
            logger.error(f"Error while processing incoming blog request : {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @blog_controller_router.get("/{blog_id}")
    def get_blog_by_id(self,blog_id:str , user_info:str=Depends(authentication)):
        try:
            blog_data = self.blogService.get_blog_by_id(blog_id)
            return blog_data
        except Exception as e:
            logger.error(f"Error while fetching blog data by id : {e}")
            raise HTTPException(status_code=500, detail=str(e))