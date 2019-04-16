#!/bin/bash

python manage.py migrate

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn async.wsgi:application \
    --worker-class=gevent \
    --worker-connections=1000 \
    --bind 0.0.0.0:8000 \
    --workers 1