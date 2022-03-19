from typing import Optional

from fastapi import FastAPI
from os import environ
import json
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "master": environ['MASTER_NAME']}


@app.post("/vibe/", status_code=200)
def post_root(payload: Optional[str] = None):
    try:
        payload = json.loads(payload)
        events = payload['events']
        for event in events:
            if event['type'] is not 'message':
                continue
            reply_token = event['replyToken']
            user_id = event['source']['userId']
            message = event['message']['text']

            messages = {
                "type": "text",
                "text": "user_id: {}\noriginal_message: {}".format(user_id, message)
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(environ['CHANNEL_ACCESS_TOKEN'])
            }
            body = {
                'replyToken': reply_token,
                'messages': messages
            }
            requests.post(url='https://api.line.me/v2/bot/message/reply', headers=headers, data=body)
    except:
        pass
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}