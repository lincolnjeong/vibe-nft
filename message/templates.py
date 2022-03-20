import json


def make_image(images):
    if len(images) == 1:
        return [{
            "type": "image",
            "url": images[0],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "300:196",
            "gravity": "center",
            "flex": 1
        }]
    elif len(images) == 2:
        return [
            {
                "type": "image",
                "url": images[0],
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
                        "url": str(images[1]),
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:196",
                        "gravity": "center"
                    }
                ],
                "flex": 1
            }
        ]
    elif len(images) >= 3:
        return [
            {
                "type": "image",
                "url": str(images[0]),
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
                        "url": str(images[1]),
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                    },
                    {
                        "type": "image",
                        "url": images[2],
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                    }
                ],
                "flex": 1
            }
        ]


template = """
{
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
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip7.jpg",
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
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip8.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center"
              },
              {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip9.jpg",
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
                    "text": " | "
                  },
                  {
                    "type": "span",
                    "text": "도끼 블랙넛 어쩌구 저쩌구"
                  }
                ],
                "size": "sm",
                "wrap": true
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [
                      {
                        "type": "span",
                        "text": "위 정보로 NFT가 발행되었습니다."
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
                        "size": "sm",
                        "color": "#bcbcbc",
                        "contents": [
                          {
                            "type": "span",
                            "text": "Maker",
                            "weight": "bold"
                          },
                          {
                            "type": "span",
                            "text": " | "
                          },
                          {
                            "type": "span",
                            "text": "maker_info"
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
                        "size": "sm",
                        "color": "#bcbcbc",
                        "contents": [
                          {
                            "type": "span",
                            "text": "Tx Hash",
                            "weight": "bold"
                          },
                          {
                            "type": "span",
                            "text": " | "
                          },
                          {
                            "type": "span",
                            "text": "tx_info"
                          }
                        ]
                      }
                    ],
                    "spacing": "none",
                    "margin": "none"
                  }
                ]
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
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "토큰 확인",
          "uri": "https://explorer.blockchain.line.me/cashew/transaction/"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "음악 듣기",
          "uri": "https://vibe.naver.com/"
        }
      }
    ]
  }
}
"""


def get_template():
    return json.loads(template)


def message_contents(msg):
    print('msg----------')
    print(msg)
    print('-------------')
    images = msg['image']
    template = get_template()
    template['body']['contents'][0]['contents'] = make_image(images)
    template['body']['contents'][1]['contents'][0]['contents'][0]['contents'][2]['text'] = msg['track_info']
    template['body']['contents'][1]['contents'][0]['contents'][1]['contents'][1]['contents'][0]['contents'][2]['text'] = msg['user_info']
    print('---------------')
    print(template)
    print('---------------')
    return template
