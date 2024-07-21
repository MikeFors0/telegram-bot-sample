# FROM python:3.10-slim-buster as python-base

# ENV PYTHONUNBUFFERED=1 \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_NO_CACHE_DIR=off \
#     USE_DOCKER=1 \
# 	# poetry:
# 	POETRY_VERSION=1.2.0 \
# 	POETRY_VIRTUALENVS_CREATE=false \
# 	POETRY_CACHE_DIR='/var/cache/pypoetry'

# RUN apt-get update \
#  && apt-get install -y build-essential gcc \
#  && pip install "poetry==$POETRY_VERSION" && poetry --version

# WORKDIR /app
# COPY ./poetry.lock ./pyproject.toml /app/


# FROM python-base as without-dev

# RUN poetry install

# COPY ./compose/production/bot/start.sh /app/
# RUN chmod +x /app/*.sh

# COPY ./src /app/src
# WORKDIR /app/src

# COPY ./pkg /app/pkg
# WORKDIR /app/pkg

# COPY ./setup.cfg ./.env /app/

# WORKDIR /app/src
FROM python:3.9-slim

RUN pip3 install poetry

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry install

COPY ./compose/production/bot/start.sh /app/
RUN chmod +x /app/*.sh

COPY ./src /app/src
WORKDIR /app/src

COPY ./pkg /app/pkg
WORKDIR /app/pkg

COPY ./setup.cfg ./.env /app/

WORKDIR /app/src