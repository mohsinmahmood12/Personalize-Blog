# BlogWise AI

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-purple)
![Celery](https://img.shields.io/badge/celery-latest-orange)

An intelligent content generation platform that creates personalized blogs using AI. Built with FastAPI, Celery, and modern Python practices.

## 🏗️ Project Structure

```
blogwise-ai/
├── personal-blog/
│   ├── controllers/
│   │   ├── blog_controller.py     # Blog-related endpoints
│   │   └── user_controller.py     # User management endpoints
│   ├── dtos/
│   │   ├── blog_dto.py           # Blog data transfer objects
│   │   ├── custom_response.py     # Response models
│   │   └── user_dto.py           # User data transfer objects
│   ├── entity_manager/
│   │   ├── logger.py             # Logging configuration
│   │   └── manager.py            # Database management
│   ├── middlewares/
│   │   └── auth.py               # Authentication middleware
│   ├── repositories/
│   │   ├── blog_repository.py    # Blog data access
│   │   └── user_repository.py    # User data access
│   ├── services/
│   │   ├── blog_service.py       # Blog business logic
│   │   └── user_service.py       # User business logic
│   ├── utils/
│   │   └── utilities.py          # Helper functions
│   ├── celery_worker.py          # Celery configuration
│   ├── main.py                   # Application entry point
│   └── websocket_manager.py      # WebSocket handling
├── tests/
├── docker-compose.yaml           # Docker configuration
├── poetry.lock                   # Dependency lock file
├── pyproject.toml               # Project configuration
└── README.md
```

## ✨ Features

- 🤖 **AI Content Generation**: Automated blog content creation
- 🔄 **Real-time Updates**: WebSocket integration for live updates
- 🔐 **Authentication**: Secure user management
- 📝 **Blog Management**: Complete CRUD operations
- 🚀 **Async Processing**: Background task handling with Celery
- 📊 **Clean Architecture**: Repository pattern implementation

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Task Queue**: Celery
- **Authentication**: JWT
- **Real-time**: WebSockets
- **Package Manager**: Poetry
- **Containerization**: Docker

## 🚀 Quick Start

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/blogwise-ai.git
cd blogwise-ai
```

2. **Install dependencies**:
```bash
poetry install
```

3. **Set up environment variables**:
```bash
cp .env.example .env
# Configure your environment variables
```

4. **Run with Docker**:
```bash
docker-compose up --build
```

Or **run locally**:
```bash
# Terminal 1: Start the FastAPI server
poetry run uvicorn personal-blog.main:app --reload

# Terminal 2: Start Celery worker
poetry run celery -A personal-blog.celery_worker worker --loglevel=info
```

## 📚 API Documentation

Once running, access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔧 Configuration

Key environment variables:

```env
DATABASE_URL=postgresql://user:pass@localhost:5432/blogwise
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key
```

## 🧪 Testing

Run the test suite:
```bash
poetry run pytest
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests
4. Commit your changes
5. Push and create a Pull Request

## 📝 Code Structure

- **Controllers**: Handle HTTP requests and responses
- **DTOs**: Define data transfer objects
- **Entity Manager**: Database connection and management
- **Middlewares**: Request/Response processing
- **Repositories**: Data access layer
- **Services**: Business logic
- **Utils**: Helper functions
- **WebSocket Manager**: Real-time communication

## 🔐 Security

- JWT Authentication
- Role-based access control
- Request validation
- Rate limiting
