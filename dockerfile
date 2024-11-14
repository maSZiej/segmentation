FROM python:3.11.5-slim-bullseye

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY .requirements.txt /app/