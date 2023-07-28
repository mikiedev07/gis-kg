FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql \
        postgis \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt