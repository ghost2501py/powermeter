#!/usr/bin/env bash
python manage.py migrate
chown www-data:www-data db.sqlite3
(gunicorn powermeter.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
