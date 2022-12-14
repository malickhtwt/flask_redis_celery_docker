FROM python:3.7.5-slim-buster

#--no-install-recommend removes unwanted packages when downloading dependencies to free up disk space
RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

# Run commands from /flask_redis_celery_docker directory inside container
WORKDIR /flask_redis_celery_docker

# Copy requirements from local to docker image
COPY requirements.txt /flask_redis_celery_docker

# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir

#RUN py.test --cov-report xml --cov ../flask_redis_celery_docker -v
#RUN coverage run -m pytest -rap  --junitxml coverage.xml
#RUN coverage xml -i

# Copy everything from the current dir to the image
COPY . .
