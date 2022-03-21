import json
import random
import string
import time
import requests
import os

from signature_generator import SignatureGenerator


def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent="\t")
    print('done to {}'.format(file_path))


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def get_track_meta(query):
    url = f'https://apis.naver.com/vibeWeb/musicapiweb/v3/search/track.json?query={query}&start=1&display=100&sort=RELEVANCE'
    meta = requests.get(url).json()['response']['result']['tracks'][0]
    track_id = meta['trackId']
    track_title = meta['trackTitle']
    artist_name = ", ".join([i['artistName'] for i in meta['artists']])
    album_title = meta['album']['albumTitle']
    album_image = meta['album']['imageUrl']
    return {'track_id': track_id, 'track_title': track_title, 'artist_name': artist_name, 'album_title': album_title,
            'album_image': album_image}


def message_analyzer(original):
    if original[:6] != '/mint ':
        return 0, original
    text = original.replace('/mint ', '')
    text = text.split(',')
    result = []
    for query in text:
        try:
            meta = get_track_meta(query)
            result.append(meta)
        except:
            pass
    if len(result) == 0:
        return 400, original
    return 200, result


def make_msg(track_info, user_info):
    return {'image': [i['album_image'] for i in track_info],
            'track_info': ", ".join([" - ".join([i['track_title'], i['artist_name']]) for i in track_info]),
            'user_id': user_info['user_id'], 'user_name': user_info['display_name'], 'track_ids': str([int(i['track_id']) for i in track_info])[1:-1].replace(' ', '')}


def load_config():
    config = {'service_api_key': os.environ['SERVICE_API_KEY'], 'service_api_secret': os.environ['SERVICE_API_SECRET'],
              'wallet_addr': os.environ['WALLET_ADDR'], 'wallet_secret': os.environ['WALLET_SECRET'],
              'contract_id': os.environ['CONTRACT_ID'], 'endpoint': os.environ['ENDPOINT']}
    return config


class BlockChainUtils:
    def __init__(self, config):
        sg = SignatureGenerator()
        self.get_signature = sg.generate
        self.config = config

    def get_headers(self, path, method, body=None):
        nonce = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
        timestamp = int(round(time.time() * 1000))
        headers = {
            'service-api-key': self.config['service_api_key'],
            'nonce': nonce,
            'timestamp': str(timestamp),
            'signature': self.get_signature(method=method, path=path, nonce=nonce, timestamp=timestamp,
                                            secret=self.config['service_api_secret'],
                                            body=body) if body is not None else self.get_signature(method=method,
                                                                                                   path=path,
                                                                                                   nonce=nonce,
                                                                                                   timestamp=timestamp,
                                                                                                   secret=self.config[
                                                                                                       'service_api_secret'])
        }
        return headers

    def get_api(self, path):
        headers = self.get_headers(path, method='GET')
        return requests.get(self.config['endpoint'] + path, headers=headers)

    def post_api(self, path, request_body):
        headers = self.get_headers(path, method='POST', body=request_body)
        return requests.post(self.config['endpoint'] + path, headers=headers, json=request_body)

    def mint_nft(self, user_id, name, meta):
        contract_id = self.config['contract_id']
        token_type = '10000001'
        path = f"/v1/item-tokens/{contract_id}/non-fungibles/{token_type}/mint"

        request_body = {
                'ownerAddress': self.config['wallet_addr'],
                'ownerSecret': self.config['wallet_secret'],
                'toUserId': os.environ['UID'],
                'name': name,
                'meta': meta
            }

        return self.post_api(path, request_body)
