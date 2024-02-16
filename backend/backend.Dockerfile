# Backend Dockerfile
FROM python:3.9

WORKDIR /app

COPY backend_requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:my_app", "--host", "0.0.0.0", "--port", "8000"]
