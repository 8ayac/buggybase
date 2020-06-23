FROM python:3.8.3-alpine3.12

LABEL "repository"="https://github.com/8ayac/buggybase"
LABEL "maintainer"="8ayac"

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

ENV APP_DIR /buggybase
COPY buggybase/ $APP_DIR/buggybase
COPY MANIFEST.in $APP_DIR
COPY setup.cfg $APP_DIR
COPY setup.py $APP_DIR

WORKDIR $APP_DIR
RUN python setup.py install --user

ENV PATH $PATH:/root/.local/bin