#!/bin/bash

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

mkdir -p /appdir/logs/
touch /appdir/logs/gunicorn.log
touch /appdir/logs/access.log
touch /appdir/logs/error.log
tail -n 0 -f /appdir/logs/*.log &

NAME='appdir'
NUM_WORKERS=3
DJANGO_WSGI_MODULE=aforos.wsgi
LOGFILE=/appdir/logs/gunicorn.log
ACCESS_LOGFILE=/appdir/logs/access.log
ERROR_LOGFILE=/appdir/logs/error.log

echo 'Starting $NAME as `whoami`'

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind 0.0.0.0:8000 \
  --log-level=info \
  --log-file=$LOGFILE \
  --access-logfile=$ACCESS_LOGFILE \
  --error-logfile=$ERROR_LOGFILE \

