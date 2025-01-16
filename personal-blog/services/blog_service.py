from content_gpt_backend.repositories.blog_repository import BlogRepository
from content_gpt_backend.dtos.blog_dto import blog , blog_input
from fastapi import Depends

class BlogService:
    def __init__(self):
        self.blogRepository = BlogRepository()

    def process_blog_request(self, blog_request: blog_input , user_info:dict):
        return self.blogRepository.add_blog_request_to_celery(blog_request , user_info)
    
    def get_blog_by_id(self,blog_id):
        return self.blogRepository.get_blog(blog_id)
        