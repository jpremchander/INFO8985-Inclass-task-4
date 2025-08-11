# Dockerfile for rolldice.py Flask app
FROM python:3.8-slim

WORKDIR /app

COPY rolldice.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "rolldice.py"]
