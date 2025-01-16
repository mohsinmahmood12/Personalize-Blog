from pydantic import BaseModel
import datetime
from fastapi import FastAPI, Response , HTTPException
from fastapi.responses import JSONResponse


USER_CREATED_RESPONSE = JSONResponse(content={"Message":"User registered successfully"},  status_code=200)
INVALID_CREDENTIALS = HTTPException(status_code=401, detail="Incorrect email or password")
BLOG_IN_PROGRESS = JSONResponse(content={"Message":"Your blog generatation is under progress. Kindly wait."},  status_code=200)