from content_gpt_backend.repositories.user_repository import UserRepository
from content_gpt_backend.dtos.user_dto import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

class UserService:
    def __init__(self):
        self.userRepository = UserRepository()

    def register(self, user: User):
        return self.userRepository.register(user)

    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        
        if not self.userRepository.is_password_correct(form_data): return {"access_token": None, type: "bearer"}
        access_token = self.userRepository.get_access_token(form_data)

        return {"access_token": access_token, "token_type": "bearer"}

    def get_all_blogs_by_user(self, email:str):
        return self.userRepository.get_all_blogs_by_user(email)
    
    def get_user_by_email(self,emal:str):
        return self.userRepository.get_user(emal)
