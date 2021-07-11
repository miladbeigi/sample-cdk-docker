ARG ALPINE_VERSION=3.13
ARG AWS_CDK_VERSION=1.105.0

FROM alpine:${ALPINE_VERSION}

RUN apk -v --no-cache --update add \
        nodejs \
        npm \
        python3 \
        py3-pip \
        ca-certificates \
        groff \
        less \
        bash \
        make \
        curl \
        wget \
        zip \
        git \
        && \
    update-ca-certificates && \
    npm install -g aws-cdk@${AWS_CDK_VERSION} && \
    pip3 install awscli

WORKDIR /opt/app

COPY setup.py requirements.txt /opt/app/
COPY cdk_docker_sample /opt/app/cdk_docker_sample

RUN pip3 install -r requirements.txt

COPY . /opt/app