import os
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, \
    StickerSendMessage, FlexSendMessage
from pydantic import BaseModel

from message.templates import message_contents
from utils import get_track_meta, message_analyzer, make_msg

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


def get_user_info(user_id):
    user_info = {}
    profile = line_bot_api.get_profile(user_id)
    user_info['display_name'] = profile.display_name
    user_info['user_id'] = profile.user_id
    user_info['picture_url'] = profile.picture_url
    user_info['status_message'] = profile.status_message
    return user_info


@router.post("/line/vibe")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(event)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    user_info = get_user_info(event.source.user_id)
    status, msg = message_analyzer(event.message.text)
    tx_id = '4D696C7B28918870EB6025F30E6B5A4577417E5613E6FAF230DB3EDA8C83CD5E'

    if status == 400:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'"{msg}" 에서 곡을 찾지 못했습니다. \n,(comma)를 사용하여 검색어를 입력해 주세요.')
        )
    elif status == 200:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text='nft message',
                contents=message_contents(make_msg(msg, user_info, tx_id))
            )
        )


@handler.add(MessageEvent, message=StickerMessage)
def sticker_text(event):
    # Judge condition
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id='6136', sticker_id='10551379')
    )
