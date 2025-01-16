from fastapi import Request , HTTPException
from entity_manager.logger import logger
import jwt
import os

def authentication(request: Request):
    try:
        bearer_token = request.headers['Authorization']
        encoded_token = bearer_token.split(" ")[1]
        information = jwt.decode(encoded_token, os.environ.get("SECRET_KEY"), algorithms=[os.environ.get("ALGORITHM")])
        return information
    except Exception as e:
        # logger.error(f"Cannot authenticate request : {e}")
        raise HTTPException(status_code=401, detail="Not Authorized")