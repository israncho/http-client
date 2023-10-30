# Dockerfile
FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install -y python3 python-pip
ADD src/http_client.py /opt/
