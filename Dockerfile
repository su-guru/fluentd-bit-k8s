FROM python:3.9-slim
WORKDIR /app
COPY log_generator.py .
CMD ["python", "log_generator.py"]