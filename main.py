import logging

import os
from os import environ
from typing import List, Optional
import requests
import json

from fastapi import FastAPI, APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, \
    StickerSendMessage
from pydantic import BaseModel

app = FastAPI()
logger = logging.getLogger("app")

#
# line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
# handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))
#
#
#
#
#
# class Line(BaseModel):
#     destination: str
#     events: List[Optional[None]]
#
#
# @router.post("/line")
# async def callback(request: Request, x_line_signature: str = Header(None)):
#     body = await request.body()
#     try:
#         handler.handle(body.decode("utf-8"), x_line_signature)
#     except InvalidSignatureError:
#         raise HTTPException(status_code=400, detail="chatbot handle body error.")
#     return 'OK'
#
#
# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     print("!!!!!!!!!!!!!!!!!!!!!!")
#     print(event)
#     print("!!!!!!!!!!!!!!!!!!!!!!")
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text)
#     )
#
#
# @handler.add(MessageEvent, message=StickerMessage)
# def sticker_text(event):
#     # Judge condition
#     line_bot_api.reply_message(
#         event.reply_token,
#         StickerSendMessage(package_id='6136', sticker_id='10551379')
#     )
#

class Item(BaseModel):
    pass
    
@app.get("/")
def read_root():
    return {"Hello": "World", "master": environ['MASTER_NAME']}


@app.post("/vibe/", status_code=200)
def post_root(item: Item):
    events = item.events
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
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}