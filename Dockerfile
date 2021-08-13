FROM python:3.9.6-alpine

WORKDIR /app

RUN pip3 install pydantic python-telegram-bot requests 

COPY . .
CMD ["python3", "main.py"]
