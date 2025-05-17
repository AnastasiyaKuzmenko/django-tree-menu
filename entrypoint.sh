#!/bin/bash

echo "🛠 Running database migrations..."
python3 /app/manage.py migrate

echo "🚀 Starting server..."
exec python3 /app/manage.py runserver 0.0.0.0:8000
