### Command to run celery worker
cd content_gpt_backend && poetry run python3 -m  celery -A content_gpt_backend.celery_worker worker --concurrency=2 --loglevel=info

### Command to run main server
poetry run python3 content_gpt_backend/main.py 