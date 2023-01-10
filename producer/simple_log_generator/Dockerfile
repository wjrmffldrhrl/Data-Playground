FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk update && \
        apk add --no-cache \
        bash

# python 기본 패키지
RUN apk add --update build-base python3-dev py-pip

RUN pip3 install -r requirements.txt

COPY main.py ./

ENTRYPOINT ["python" , "/usr/src/app/main.py"]


