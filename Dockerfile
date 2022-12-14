FROM python:3.7

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/appdir

RUN mkdir $WEBAPP_DIR
WORKDIR $WEBAPP_DIR

COPY . $WEBAPP_DIR/

RUN pip install -r requirements.txt