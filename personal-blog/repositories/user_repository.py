from content_gpt_backend.repositories.user_interface_repository import IUserRepository
from content_gpt_backend.entity_manager.manager import entity_manager
from content_gpt_backend.dtos.user_dto import User
import os
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from passlib.context import CryptContext
from datetime import timedelta
from passlib.hash import bcrypt
from datetime import datetime
import jwt
from jwt import PyJWTError
from fastapi import HTTPException


# CryptContext for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository(IUserRepository):
    def __init__(self):
        self.user_collection = entity_manager.get_collection("users")
        self.blog_collection = entity_manager.get_collection("blogs")
    
    def register(self, user : User):
        usr = self.user_collection.find_one({"email": user.email})
        if usr is None:
            self.user_collection.insert_one(
                {
                    "username":user.username,
                    "email": user.email,
                    "password": bcrypt.using(rounds=12).hash(user.password),
                    "blogs_count":0
                }
            )
            return user
        else:
            return False

    def create_access_token(self, data: dict, expires_delta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.environ.get("SECRET_KEY"), algorithm=os.environ.get("ALGORITHM"))
        return encoded_jwt

    def get_user(self, email: str):
        usr = self.user_collection.find_one({"email": email},{"password":0})

        if usr is not None:
            usr["_id"] = str(usr["_id"])
            return usr
        
        return None

    def is_password_correct(self, form_data: OAuth2PasswordRequestForm = Depends()) -> bool:
        user = self.user_collection.find_one({"email": form_data.username})
        if user is None or not pwd_context.verify(form_data.password, user["password"]):
            return False

        return True

    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):        
        access_token_expires = timedelta(minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")))
        usr = self.user_collection.find_one({"email": form_data.username})
        access_token = self.create_access_token(
            data={"email": form_data.username ,"username":usr["username"],"blogs_count":usr["blogs_count"], "id":str(usr["_id"])}, expires_delta=access_token_expires
        )
        return access_token

    def get_all_blogs_by_user(self, email:str):
        all_blogs = self.blog_collection.find({"user_email":email},{"content":0})
        all_blogs_list = []
        for blog in all_blogs:
            blog["_id"] = str(blog["_id"])
            all_blogs_list.append(blog)
        return all_blogs_list

   
