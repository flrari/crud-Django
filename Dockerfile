FROM python:latest

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/
EXPOSE 8000

COPY wait.sh /wait.sh
RUN chmod +x /wait.sh