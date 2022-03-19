import json
import random
import string
import time

import requests

from signature_generator import SignatureGenerator


def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent="\t")
    print('done to {}'.format(file_path))


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


class Utils:
    def __init__(self, config):
        sg = SignatureGenerator()
        self.get_signature = sg.generate
        self.config = config

    def get_api(self, path):
        nonce = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
        timestamp = int(round(time.time() * 1000))
        headers = {
            'service-api-key': self.config['service_api_key'],
            'nonce': nonce,
            'timestamp': str(timestamp),
            'signature': self.get_signature(method='GET', path=path, nonce=nonce, timestamp=timestamp,
                                            secret=self.config['service_api_secret']),
        }
        return requests.get(self.config['endpoint'] + path, headers=headers)
