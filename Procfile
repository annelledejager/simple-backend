release: python manage.py migrate
release: python manage.py loaddata simple_backend/fixtures/initial_data.json
web: gunicorn simple_backend.wsgi:application --log-file -
