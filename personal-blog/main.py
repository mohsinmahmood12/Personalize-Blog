from fastapi import FastAPI , WebSocket, WebSocketDisconnect , Request
from fastapi.responses import HTMLResponse
from content_gpt_backend.websocket_manager import socket_manager
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv
from content_gpt_backend.controllers.user_controller import user_controller_router
from content_gpt_backend.controllers.blog_controller import blog_controller_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tags_metadata = [
    {"name": "Users", "description": "Operations related to user management"},
    {"name": "Blogs", "description":"Operations related to blog management"}
]


# Health-check
@app.get("/")
def health_check():
    return {"Status":"Server is up and running"}


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await socket_manager.connect(websocket, user_id)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        socket_manager.disconnect(websocket, user_id)


@app.post("/notify")
async def notify(request: Request):
    data = await request.json()
    message = data.get("message")
    user_id =  data.get("user_id")
    await socket_manager.send_personal_message(message , user_id)
    return {"status": "sent"}


# Include the routers from controller modules
app.include_router(user_controller_router, prefix="/users", tags=["Users"])
app.include_router(blog_controller_router,prefix="/blogs",tags=["Blogs"])


if __name__ == '__main__':
    load_dotenv()
    uvicorn.run("main:app",host=os.environ.get("HOST"), port=int(os.environ.get("PORT")),reload=False)
