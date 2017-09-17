FROM python:2.7
MAINTAINER Umair Sarfraz "aquadestructor@icloud.com"

ADD . /iota-ctps
WORKDIR /iota-ctps

RUN pip install --upgrade pip
RUN pip install -r /iota-ctps/requirements.txt
