import json
import os


def get_template():
    return json.loads(os.environ['DEFAULT_TEMPLATE'])


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


def message_contents(msg):
    images = msg['image']
    template = get_template()
    template['body']['contents'][0]['contents'] = make_image(images)
    template['body']['contents'][1]['contents'][0]['contents'][0]['contents'][2]['text'] = msg['track_info']
    template['body']['contents'][1]['contents'][0]['contents'][1]['contents'][1]['contents'][0]['contents'][2]['text'] = msg['user_name']
    template['body']['contents'][1]['contents'][0]['contents'][1]['contents'][2]['contents'][0]['contents'][2]['text'] = msg['user_id']
    template['body']['contents'][1]['contents'][0]['contents'][1]['contents'][3]['contents'][0]['contents'][2]['text'] = msg['tx_id']
    template['footer']['contents'][0]['action']['uri'] += msg['tx_id']
    template['footer']['contents'][1]['action']['uri'] += msg['track_ids']
    return template
