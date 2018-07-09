#!/bin/sh

git clone https://github.com/code500info/code500web.git

cd code500web

python manage.py runserver 5000 &