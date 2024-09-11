#!/bin/sh

sleep 10

python manage.py migrate
python manage.py createcachetable
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@gmail.com', 'it12345')"
python manage.py initialize_db
python manage.py collectstatic  --noinput
gunicorn it_profi.wsgi:application --bind 0.0.0.0:8000

exec "$@"