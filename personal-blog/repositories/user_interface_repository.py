from abc import abstractmethod
from content_gpt_backend.dtos.user_dto import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

class IUserRepository:
    @abstractmethod
    def register(self, user : User) -> User: pass

    @abstractmethod
    def create_access_token(self, data: dict, expires_delta): pass

    @abstractmethod
    def get_user(self, username: str): pass

    @abstractmethod
    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()): pass

    @abstractmethod
    def is_password_correct(self, form_data: OAuth2PasswordRequestForm = Depends()) -> bool: pass

    @abstractmethod
    def get_all_blogs_by_user(self, user_id:str) -> dict: pass
