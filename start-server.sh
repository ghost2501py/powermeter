#!/usr/bin/env bash
(gunicorn powermeter.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
