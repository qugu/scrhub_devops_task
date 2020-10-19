FROM ubuntu:xenial

COPY serve.py /serve.py
COPY requirements.txt /requirements.txt
RUN apt-get update -y && apt-get install python3 python3-pip -y
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/bin/python3", "/serve.py"]