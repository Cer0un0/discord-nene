import json
import os
import requests
from json.decoder import WHITESPACE


def get_environvar(key: str) -> str:
    """ 環境変数を返す

    @args
        key (str): 変数名
    @returns:
        str: 値
    """
    try: # heroku
        return os.environ[key]
    except: # local
        with open('../data/environment_vars.json') as f:
            vars = json.load(f)
        return vars[key]

def loads_iter(s):
    size = len(s)
    decoder = json.JSONDecoder()

    end = 0
    while True:
        idx = WHITESPACE.match(s[end:]).end()
        i = end + idx
        if i >= size:
            break
        ob, end = decoder.raw_decode(s, i)
        yield ob

async def post_webhook(message,  content: str):
    webhooks = await message.channel.webhooks()

    if not webhooks:
        await message.channel.create_webhook(name='unbobo-webhook')
        webhooks = await message.channel.webhooks()

    webhook_url = webhooks[0].url

    main_content = {
        "username": message.author.display_name,
        "avatar_url": str(message.author.avatar_url),
        "content": content
    }

    requests.post(webhook_url, main_content)