#!/bin/bash

# go to backend directory
cd backend

# activate the python environment
source venv/bin/activate

# run the app
gunicorn -w 1 --bind 0.0.0.0:5001 wsgi
