# インストールした discord.py を読み込む
import discord
import sys
import requests
import random as ra
import os

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ["TOKEN"]

# 接続に必要なオブジェクトを生成
client = discord.Client()
#unko

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

    channel = client.get_channel(int(os.environ["CHANNEL_DEVROOM"]))
    await channel.send("墨です!!!おはようございます!!!!!")
# メッセージ受信時に動作する処理


async def weather(S):
    print('unko')
    url = build_url(S)
    json_data = request_json(url)
    print(json_data)
    in_one_hour_rainfall = extract_rainfall(json_data)
    print(json_data)
    return json_data


    if in_one_hour_rainfall >= 10:
        rainfall_notice = notification_level(in_one_hour_rainfall)


# url組み立て
def build_url(S):
    APP_ID = "dj00aiZpPU4wM2tLc1hIREZWWiZzPWNvbnN1bWVyc2VjcmV0Jng9ZDU-"
    BASE_URL = "http://weather.olp.yahooapis.jp/v1/place"
    if S[1] == 'Osaka' or S[1] == 'O':
        COORDINATES = '34.691576, 135.506632'
    elif S[1] == 'Hakata' or S[1] == 'H':
        COORDINATES = '33.589412, 130.421062'
    elif S[1] == 'Machida' or S[1] == 'M':
        COORDINATES = '35.541994, 139.445376'
    elif S[1] == 'Kawasaki' or S[1] == 'K':
        COORDINATES = '35.530833, 139.702912'
    else: return 'Osaka(O), Hakata(H), Machida(M), Kawasaki(K)から選んでね'
    OUTPUT = "json"

    url = BASE_URL + "?appid=%s&coordinates=%s&output=%s" % (APP_ID, COORDINATES, OUTPUT)

    return url


# リクエスト
def request_json(url):
    req = requests.get(url)
    json_data = req.json()

    return json_data


# 降水強度の取得
def extract_rainfall(json_data):
    weather = json_data['Feature'][0]['Property']['WeatherList']['Weather']
    in_one_hour_rainfall = weather[1]['Rainfall']
    print(json_data)
    return json_data

    return in_one_hour_rainfall




@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith('!nene'):
        await client.logout()
        await sys.exit()
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    elif message.content == '/oshioki':
        x = ra.randint(0, 1)
        return_message = ''
        if x == 0:
            return_message = 'もう、カノジョをこんなにほうっておくなんて。\nオシオキが必要なんじゃない？'
        elif x == 1:
            return_message = '今まで何してたの？・・・もう。'

        await message.channel.send(return_message)

    elif message.content == '/sumi':
        f = open('sumi', 'r')
        line = f.readlines()
        url = []
        for i in range(len(line)):
            url.append(line[i].replace('\n', ''))
        x = ra.randint(0, len(url)-1)
        return_message = url[x]

        await message.channel.send(return_message)
    elif message.content == '/ruka':
        f = open('ruka', 'r')
        line = f.readlines()
        url = []
        for i in range(len(line)):
            url.append(line[i].replace('\n', ''))
        x = ra.randint(0, len(url)-1)
        return_message = url[x]

        await message.channel.send(return_message)

    elif '/tenki' in message.content:
        if ' ' not in message.content: await message.channel.send('Osaka(O), Hakata(H), Machida(M), Kawasaki(K)から選んでね')
        else:
            S = message.content[1:].split(' ')
            await message.channel.send(weather(S))
        print('ochinpo')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


