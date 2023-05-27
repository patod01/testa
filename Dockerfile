FROM python:3.11.2-alpine3.17
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt
RUN mkdir db
CMD python papp.py
