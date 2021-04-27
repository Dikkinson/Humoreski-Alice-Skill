FROM python:2.7.14-alpine

WORKDIR /app
COPY python/buy-elephant/now /app

EXPOSE 5000

RUN pip install -r requirements.txt
CMD FLASK_APP=api.py flask run --host="::"
