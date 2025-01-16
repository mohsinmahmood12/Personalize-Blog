from fastapi import HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from content_gpt_backend.services.user_service import UserService
from content_gpt_backend.dtos.user_dto import User
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from content_gpt_backend.dtos.custom_response import USER_CREATED_RESPONSE
from content_gpt_backend.middlewares.auth import authentication

user_controller_router = InferringRouter()

@cbv(user_controller_router)
class UserController:
    def __init__(self): 
        self.userService = UserService()

    @user_controller_router.post("/register")
    def register(self, user: User):
        try:
            usr = self.userService.register(user)
            if usr is not False:
                return USER_CREATED_RESPONSE
            else:
                raise HTTPException(status_code=422, detail="User already exists")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @user_controller_router.post("/login")
    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        try:
            access_token = self.userService.get_access_token(form_data)
            # print(access_token)
            if access_token["access_token"] is None:
                raise HTTPException(status_code=401, detail="Incorrect username or password")
            return access_token
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))

    @user_controller_router.get("/all_blogs")
    def get_blogs(self, user_info:str=Depends(authentication)):
        try:
            all_blogs = self.userService.get_all_blogs_by_user(user_info["email"])
            return {"blogs":all_blogs}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @user_controller_router.get("/user_details")
    def get_user(self, user_info:str=Depends(authentication)):
        try:
            user_details = self.userService.get_user_by_email(user_info["email"])
            return user_details
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


