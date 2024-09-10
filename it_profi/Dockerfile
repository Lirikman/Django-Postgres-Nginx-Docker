FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

#RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y curl && apt-get clean

RUN pip install -r requirements.txt

CMD python manage.py migrate \
   && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@gmail.com', 'it12345')" \
   && python manage.py initialize_db \
   && python manage.py collectstatic --no-input \
   && gunicorn it_profi.wsgi:application --bind 0.0.0.0:5000