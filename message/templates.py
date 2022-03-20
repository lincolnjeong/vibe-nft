import json


def make_image(images):
    if len(images) == 1:
        return json.dumps({
            "type": "image",
            "url": str(images[0]),
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "300:196",
            "gravity": "center",
            "flex": 1
        })
    elif len(images) == 2:
        return [{
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
                        "aspectRatio": "150:196",
                        "gravity": "center"
                    }
                ],
                "flex": 1
            }
        }]
    elif len(images) >= 3:
        return json.dumps([{
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
                        "url": str(images[2]),
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                    }
                ],
                "flex": 1
            }
        }])


def message_contents(msg):
    print('msg----------')
    print(msg)
    print('-------------')
    return {
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
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip13.jpg",
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
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
                    "text": "brown_05",
                    "weight": "bold",
                    "color": "#000000"
                  },
                  {
                    "type": "span",
                    "text": "     "
                  },
                  {
                    "type": "span",
                    "text": "I went to the Brown&Cony cafe in Tokyo and took a picture"
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
                    "text": "1,140,753 Like",
                    "size": "sm",
                    "color": "#bcbcbc"
                  }
                ],
                "spacing": "sm",
                "margin": "md"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px"
  }
}
    template = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": make_image(msg['image'])
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
                                            "text": msg['track_info']
                                        }
                                    ],
                                    "size": "sm",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "contents": [
                                        {
                                            "type": "span",
                                            "text": "위 정보로 NFT가 발행되었습니다.",
                                            "weight": "bold",
                                            "color": "#000000"
                                        }
                                    ],
                                    "size": "sm",
                                    "wrap": True
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "",
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
                                                    "text": msg['user_info']
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
                                            "text": "",
                                            "size": "sm",
                                            "color": "#bcbcbc",
                                            "contents": [
                                                {
                                                    "type": "span",
                                                    "text": "Tx ID"
                                                },
                                                {
                                                    "type": "span",
                                                    "text": " | "
                                                },
                                                {
                                                    "type": "span",
                                                    "text": msg['tx_id']
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
                        "uri": "https://explorer.blockchain.line.me/cashew/transaction/{}".format(msg['tx_id'])
                    }
                }
            ]
        }
    }
    print('---------------')
    print(template)
    print('---------------')
    return template
