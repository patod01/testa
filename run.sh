#! /bin/ash

pip install --upgrade pip
pip install --no-cache-dir -r req.txt

# python papp.py
python try.py

# docker network create alambre

# docker run --rm --network alambre -it --name mac -p 10111:10111 -w /app -v "$(pwd)":/app python:3.11.2-alpine3.17 ash run.sh

# docker run --rm --network alambre --name flan cloudflare/cloudflared:latest tunnel --no-autoupdate run --token eyJhIjoiNTMwODFhMzU3NTY5MjRiMWY5NjQ2NzYzYmEzM2RmYmQiLCJ0IjoiYTllNDdhODQtMTA1MC00MGY2LTgxZGItNjBhODA0ZDMwYTgzIiwicyI6IlptWTFaams1TXpndFpEZG1ZUzAwWmprM0xXSXlNekV0T0dReU5XTTROalF3WXpGb9
