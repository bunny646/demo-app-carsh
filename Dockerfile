
FROM python:3.14-slim
WORKDIR /app
COPY main.py .
RUN pip install flask gunicorn
CMD exec gunicorn --bind 0.0.0.0:8080 main:app
