from __future__ import unicode_literals
from random import choice
import json
import logging

from flask import Flask, request


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

with open('umorezki.txt', 'r', encoding="utf-8") as file:
    data = json.load(file)

# Хранилище данных о сессиях.
sessionStorage = {}


# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
    # Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )


# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    suggests = [
        {'title': "Следующий", 'hide': True},
    ]

    if req['session']['new']:
        res['response']['text'] = get_anek()
        res['response']['buttons'] = suggests
        return

    if req['request']['original_utterance'].lower() in [
        'следующий'
    ]:
        res['response']['text'] = get_anek()
        res['response']['buttons'] = suggests
        return

    res['response']['text'] = ''
    res['response']['buttons'] = suggests


def get_anek():
    return choice(data)
