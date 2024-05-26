#!/bin/sh

# Initialize the database
airflow db init

# Start the web server or scheduler
exec airflow "$@"
