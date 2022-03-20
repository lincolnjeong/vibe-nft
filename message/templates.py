def make_image(images):
    if len(images) == 1:
        return {
            "type": "image",
            "url": images[0],
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "300:196",
            "gravity": "center",
            "flex": 1
        }
    elif len(images) == 2:
        return {
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
                        "url": images[1],
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:196",
                        "gravity": "center"
                    }
                ],
                "flex": 1
            }
        }
    elif len(images) >= 3:
        return {
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
                        "url": images[1],
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
        }


def message_contents(msg):
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
                        make_image(msg['image'])
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

    return template