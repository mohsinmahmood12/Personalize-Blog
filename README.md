# Personalize-Blog

Personalize-Blog is an AI-powered platform designed to generate engaging, personalized blogs based on trending topics that matter to you. With a seamless backend architecture and advanced AI algorithms, this project empowers users to stay informed and inspired by tailored content.

## Features

- **Personalized Content**: Generate blogs based on your interests and trending topics.
- **AI-Driven**: Leverages cutting-edge AI to ensure dynamic and relevant content creation.
- **Scalable Architecture**: Built with robust tools like Celery for task management and Poetry for streamlined dependency management.
- **Dockerized**: Easily deploy the project with Docker and docker-compose for a hassle-free setup.
- **Testing Framework**: Includes a comprehensive testing suite for ensuring code quality and reliability.

## Project Structure

```
Personalize-Blog/
├── content_gpt_backend/
│   ├── celery_worker.py    # Celery worker configurations
│   ├── main.py            # Main application server
│   ├── tasks/            # AI tasks and background jobs
│   ├── utils/            # Utility scripts
├── tests/                # Test cases and testing framework
├── docker-compose.yaml    # Docker configuration
├── poetry.lock           # Dependency lockfile
├── pyproject.toml        # Poetry project configuration
└── README.md            # Project documentation
```

## Prerequisites

- **Python**: Ensure Python 3.8+ is installed.
- **Poetry**: Dependency management tool.
- **Docker**: For containerized deployment.
- **Redis**: Required for Celery task queue.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mohsinmahmood12/Personalize-Blog.git
   cd Personalize-Blog
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Set up the environment variables**:
   Create a `.env` file in the root directory and add the required configuration.

4. **Run database migrations** (if applicable):
   ```bash
   poetry run python3 content_gpt_backend/manage.py migrate
   ```

## Commands

### Running Celery Worker

Run the Celery worker for handling background tasks:
```bash
cd content_gpt_backend && poetry run python3 -m celery -A content_gpt_backend.celery_worker worker --concurrency=2 --loglevel=info
```

### Running the Main Server

Start the main server:
```bash
poetry run python3 content_gpt_backend/main.py
```

## Docker Deployment

1. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```

2. **Access the application**:
   Visit `http://localhost:8000` in your browser.

## Testing

Run tests to ensure everything works as expected:
```bash
poetry run pytest
```

## Contribution Guidelines

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.

