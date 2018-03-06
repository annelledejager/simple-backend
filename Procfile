release: python manage.py migrate
web: gunicorn simple_backend.wsgi:application --log-file -