FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git python3 python3-pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /root
