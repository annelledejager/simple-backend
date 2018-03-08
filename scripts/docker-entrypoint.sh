#!/bin/bash

cmd="$@"

# Wait for DB service to be ready
./scripts/wait-for db:5432

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Create new database migrations
echo "Create new database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Load initial data
echo "Load initial data"
python manage.py loaddata simple_backend/fixtures/initial_data.json

## Run command from compose file
exec $cmd
