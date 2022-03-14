FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD requirements.txt /config/
WORKDIR /app/
RUN pip3 install -r /config/requirements.txt
RUN adduser --disabled-password --gecos '' myuser  