#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Load initial data
echo "Load initial data"
python manage.py loaddata simple_backend/fixtures/initial_data.json
