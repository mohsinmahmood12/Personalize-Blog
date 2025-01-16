from abc import abstractmethod
from content_gpt_backend.dtos.blog_dto import blog_input , blog
from content_gpt_backend.dtos.user_dto import User
from fastapi.responses import JSONResponse
from fastapi import Depends

class IBlogRepository:
    @abstractmethod
    def get_blogs_by_user(self, user : User) -> list: pass

    @abstractmethod
    def add_blog_request_to_celery(blog_request:blog_input) -> JSONResponse: pass

    @abstractmethod
    def get_blog(blog_id:str) -> blog: pass
    