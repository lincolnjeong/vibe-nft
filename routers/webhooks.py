import os
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, \
    StickerSendMessage
from pydantic import BaseModel

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


@router.post("/line/vibe")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'


template = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://musicmeta-phinf.pstatic.net/album/005/141/5141786.jpg?type=r480Fll&v=202203201451",
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
            "gravity": "center",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://musicmeta-phinf.pstatic.net/album/000/194/194629.jpg?type=r480Fll&v=202203201451",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center"
              },
              {
                "type": "image",
                "url": "https://musicmeta-phinf.pstatic.net/album/005/242/5242739.jpg?type=r480Fll&v=202203201451",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center"
              }
            ],
            "flex": 1
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "Tracks",
                    "weight": "bold",
                    "color": "#000000"
                  },
                  {
                    "type": "span",
                    "text": "    | "
                  },
                  {
                    "type": "span",
                    "text": "봄비 - 라일락, 봄봄 - 아이유, 허슬허슬허슬허슬허슬 - 도끼"
                  }
                ],
                "size": "sm",
                "wrap": true
              },
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "Tracks",
                    "weight": "bold",
                    "color": "#000000"
                  },
                  {
                    "type": "span",
                    "text": "    | "
                  },
                  {
                    "type": "span",
                    "text": "봄비 - 라일락, 봄봄 - 아이유, 허슬허슬허슬허슬허슬 - 도끼"
                  }
                ],
                "size": "sm",
                "wrap": true
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Maker | U2oeoASefqwefQWEFqwef",
                    "size": "sm",
                    "color": "#bcbcbc",
                    "contents": [
                      {
                        "type": "span",
                        "text": "Maker ID"
                      },
                      {
                        "type": "span",
                        "text": " | "
                      },
                      {
                        "type": "span",
                        "text": "U1iriowef92"
                      }
                    ]
                  }
                ],
                "spacing": "sm",
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Maker | U2oeoASefqwefQWEFqwef",
                    "size": "sm",
                    "color": "#bcbcbc",
                    "contents": [
                      {
                        "type": "span",
                        "text": "Tx"
                      },
                      {
                        "type": "span",
                        "text": " | "
                      },
                      {
                        "type": "span",
                        "text": "Txdddd"
                      }
                    ]
                  }
                ],
                "margin": "none",
                "spacing": "none"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "토큰 확인",
          "uri": "http://linecorp.com/"
        }
      }
    ]
  }
}

flex_message = FlexSendMessage(
  template
)

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(event)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    message = f"msg: {event.message.text}\nuser_id: {event.source.user_id}"
    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=message)
        flex_message
    )



@handler.add(MessageEvent, message=StickerMessage)
def sticker_text(event):
    # Judge condition
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id='6136', sticker_id='10551379')
    )
