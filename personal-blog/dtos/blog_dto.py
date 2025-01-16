from pydantic import BaseModel
from datetime import datetime

class blog_input(BaseModel):
    topic: str
    instructions: str = ""

class blog(BaseModel):
    topic: str
    instructions: str
    content: str = ""
    user_email: str
    created_at: datetime
    status:str = "pending"
