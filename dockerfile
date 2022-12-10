FROM python:3.10-slim-bullseye

WORKDIR /SHORTLINK-CORE

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

