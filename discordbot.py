# インストールした discord.py を読み込む
import discord
import sys
import random as ra
import os
sys.dont_write_bytecode = True

import botutil

# 自分のBotのアクセストークンに置き換えてください
TOKEN = botutil.get_environvar('TOKEN')


# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


    channel = client.get_channel(int(botutil.get_environvar('CHANNEL_DEVROOM')))
    await channel.send("墨です!!!おはようございます!!!!!")
# メッセージ受信時に動作する処理


def ra_file_line(input_file):
    f = open(input_file, 'r')
    line = f.readlines()
    url = []
    for i in range(len(line)):
        url.append(line[i][:-1])
    x = ra.randint(0, len(url)-1)

    return url[x]

def save_py(message):

    out = open('out.py', 'w')
    lines = message.split('\n')
    print(lines)
    out.write('def do():\n')

    for line in lines[1:]:
        out.write(' '+line+'\n')
    out.close()
    return


def dekke(message, split_s): # 返すだけ
    N = 10
    x = ra.randint(0, N)
    s = message.split(split_s)
    kke_num = ra.randint(1, 20)
    ex_num = ra.randint(1, 20)
    if x<5:
        return 'すっげー' +  'ー'*kke_num + '！'*ex_num
    elif x<8:
        return 'すげーじゃねーか'
    elif x==9:
        return 'さとりのちんぽのがでっけーよ' + '！'*ex_num

    return '/washlet'


def sugge(message, split_s):
    N = 10
    x = ra.randint(0, N)
    s = message.split(split_s)
    kke_num = ra.randint(1, 20)
    ex_num = ra.randint(1, 20)
    if x<5:
        return 'でっけ' + 'ー'*kke_num + '！'*ex_num
    elif x==6:
        return 'でっかくない・・・'
    elif x==7:
        return 'でっけーわけないだろ' + '！'*ex_num
    elif x==8:
        return '/rfgacha りん・・・来い' + '！'*ex_num
    elif x==9:
        return 'さとりのちんぽのがでっけーよ' + '！'*ex_num

    return '/washlet'


@client.event
async def on_message(message):
    print(message.content)
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    elif message.content == '/oshioki':
        await message.channel.send(ra_file_line('oshioki'))
    elif '/sumi' in message.content:
        await message.channel.send(ra_file_line('sumi'))
    elif '/ruka' in message.content:
        await message.channel.send(ra_file_line('ruka'))
    elif 'すげー' in message.content:
        await message.channel.send(sugge(message.content, 'けー'))
    elif 'でっけー' in message.content:
        await message.channel.send(dekke(message.content, 'けー'))


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


