#!/usr/bin/env bash

NAME="iota-ctps"
WORKERS=2
WORKER_CLASS=eventlet

exec gunicorn app:app -b 0.0.0.0:9080 \
  --reload \
  --name $NAME \
  --workers $WORKERS \
  --worker-class $WORKER_CLASS
