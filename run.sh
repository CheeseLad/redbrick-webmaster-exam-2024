#!/bin/sh

cleanup() {
    echo "\nStopping servers..."
    if [ -n "$DJANGO1_PID" ]; then
        kill "$DJANGO1_PID"
    fi
    if [ -n "$DJANGO2_PID" ]; then
        kill "$DJANGO2_PID"
    fi
    # Terminate Vite dev server if it is running
    if [ -n "$VITE_PID" ]; then
        kill "$VITE_PID"
    fi
    exit 0
}

trap cleanup INT

python3 ./site/manage.py runserver 127.0.0.1:8000 &
DJANGO1_PID=$!

python3 ./api/manage.py runserver 127.0.0.1:8001 &
DJANGO2_PID=$!

vite --config ./site/vite.config.js &
VITE_PID=$!

wait
