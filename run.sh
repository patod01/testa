#! /bin/ash

pip install --upgrade pip
pip install --no-cache-dir -r req.txt

# python papp.py
python try.py

# docker run --rm -it --name mac -p 10111:5000 -w /app -v "$(pwd)":/app python:3.11.2-alpine3.17 ash run.sh
