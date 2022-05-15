#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import json
import uuid
import os
import requests
import humanize
import random
import pickle
import time
from time import time
from time import sleep
from pyrogram.errors import FloodWait
import os
from pyrogram import Client, filters, types, errors, emoji
from pyrogram.types import ChatPermissions
import random
import asyncio
from asyncio import sleep
import re
from io import BytesIO
import requests
import base64
from time import perf_counter
import subprocess
import wikipedia
from gtts import gTTS
from covid import Covid
from pyrogram.raw import functions
from datetime import datetime
import wikipedia
import pytz
import sys
from datetime import timedelta
from pathlib import Path
import aiohttp
from pyrogram.handlers import MessageHandler
import ast
from requests import get
from io import BytesIO
from random import randint, choice
from textwrap import wrap
from googletrans import Translator
import googletrans
from pyrogram.errors import (
    UserAdminInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UsernameInvalid,
    RPCError,
)
from pyrogram.utils import (
    get_channel_id,
    MAX_USER_ID,
    MIN_CHAT_ID,
    MAX_CHANNEL_ID,
    MIN_CHANNEL_ID,
)


async def CheckAdmin(message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await app.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("The command needs to be a reply")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message):
    await message.edit(f"I can't {message.command} this user.")
    await asyncio.sleep(2)
    await message.delete()

trl = Translator()


AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}

def GetUserMentionable(user):
    """ Get mentionable text of a user."""
    if user.username:
        username = "@{}".format(user.username)
    else:
        if user.last_name:
            name_string = "{} {}".format(user.first_name, user.last_name)
        else:
            name_string = "{}".format(user.first_name)

        username = "<a href='tg://user?id={}'>{}</a>".format(user.id, name_string)

    return username


def GetChatID(message):
    """ Get the group id of the incoming message"""
    return message.chat.id

def ReplyCheck(message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id



unoo = '''
⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇
'''
g = '''
░░░░▓█───────▄▄▀▀▀▄─────
░░░░▒░█────▄█▒░░▄░█─────
░░░░░░░▀▄─▄▀▒▀▀▀▄▄▀─────
░░░░░░░░░█▒░░░░▄▀───────
▒▒▒░░░░▄▀▒░░░░▄▀──────── 
▓▓▓▓▒░█▒░░░░░█▄───────── 
█████▀▒░░░░░█░▀▄──────── 
█████▒▒░░░▒█░░░▀▄─────── 
███▓▓▒▒▒▀▀▀█▄░░░░█────── 
▓██▓▒▒▒▒▒▒▒▒▒█░░░░█───── 
▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░░█──── 
░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░█───'''

m = '''
████████
██
██
██████
██
██
██'''

rep = '<b>Установка:</b> \n pkg install git && pkg install python && pkg update && pkg upgrade && git clone https://github.com/sempfira/Sakura.git && cd Sakura && pip install -r install.txt && python tgcmd.cpython-310.pyc \n <b>Повторный запуск</b> \n  cd Sakura && python tgcmd.cpython-310.pyc'

h = "╔┓┏╦━━╦┓╔┓╔━━╗ ║┗┛║┗━╣┃║┃║╯╰║ ║┏┓║┏━╣┗╣┗╣╰╯║ ╚┛┗╩━━╩━╩━╩━━╝"



fuckk = '''
╱▔▔▔╲┈┈┈┈┈╱▔▔▔╲
▏╰┈╮┈╲╲┈╱╱┈╭┈╯▕
╲╮┈╰┈╮╲▉╱╭┈╯┈╭╱
▕╰┈╮┈╰╮▉╭╯┈╭┈╯▏
┈╲▂╰┈┈╱▉╲┈┈╯▂╱
┈┈╱▔▔▔╭▊╮▔▔▔╲
┈┈▏╭┈┈╯▊╰┈┈╮▕
┈▕╭╯┈┈╱▋╲┈┈╰╮▏
┈┈╲▂▂╱┈┈┈╲▂▂╱
'''


class BaseDice:
    value = 0


d = ''' 
████╗███╗█╗█╗
█╔══╝█╔█║█║█║
████╗███║███║
█╔═█║█╔█║█╔█║
████║█║█║█║█║
╚═══╝╚╝╚╝╚╝╚╝
'''


db = sqlite3.connect('db.db')
sql = db.cursor()





my_id = 5155964636
j_id = 5155964636
v_id = 5155964636
bots = "vkmusic_bot"
version = '1.0.0.0'
module_list = {}
file_list = {}
app = Client('Nex1n', api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')
my_id =  5155964636
j_id = 5155964636
a_id = 5155964636
v_id = 5155964636
n_id = 5155964636
a = ["Разраб", "Админ", "Важный","DEVELOPER", "Главный", "Папочка", "Мамочка"]


sql.execute("""CREATE TABLE IF NOT EXISTS notes (
    name TEXT,
    notee TEXT
    )""")
db.commit()



sql.execute("""CREATE TABLE IF NOT EXISTS notes (name TEXT,notee TEXT,my_photo BLOB,my_name TEXT, my_sour TEXT)""")
db.commit()

db = sqlite3.connect('db.db')
sql = db.cursor()


def check_hardware_hwid():
    hwid = hex(uuid.getnode())
    print(hwid)
    r = requests.get("https://pastebin.com/4GLFKeD3")
    if hwid not in r.text:
        print("Access granted...")
        app.start()

        app.stop()
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
            
        print('''   v999
             
           ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
           ┃                                                              ┃
           ┃                                                              ┃
           ┃                                                              ┃
           ┃---------Telegram: @@sempfira---------    ┃
           ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


    ''')
        
        print("После ввода задержки напишите в любой телеграм чат команду /help для просмотра команд!")
        


        BASE_PATH = os.path.abspath(os.getcwd())

        @app.on_message(filters.command("mems", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_message(msg.chat.id, f'''
            ✨ Меню голосовых мемов:
            (Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
                
             1) Команда: ".сукаблядьнахуй"
             2) Команда: ".блядьуходиотсюда"
             3) Команда: ".татышоахуэл"
             4) Команда: ".блядьнахуй"
             5) Команда: ".щясзарежу"
             6) Команда: ".гдетыблядь"
             7) Команда: ".даунобосаный"
             8) Команда: ".ктокуда"
             9) Команда: ".уменяестьплан"
             10) Команда: ".ятрахнутебя"

            
            (Все команды нужно писать без ковычек)
            
                ''')
            global number
            number = number + 1

        @app.on_message(filters.command("сукаблядьнахуй", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems/syka-blyad-nahyi.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("блядьуходиотсюда", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems/blyat-vixodi-otsyda.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("татышоахуэл", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems/ta-ti-sho-oxyel.mp3")

        @app.on_message(filters.command("блядьнахуй", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems/nahui-blyat.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("щясзарежу", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems/schas-zareju.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("гдетыблядь", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems/gde-tyi.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("даунобосаный", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems//daun-obosannyii-mat-tvoyu-v-kanavu-kidal.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("ктокуда", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems//kto-kuda-a-ya-po-delam.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("уменяестьплан", prefixes=".") & filters.me)
        def sykatest(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems//u-menya-est-takoi-plan.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("ятрахнутебя", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "mems//ya-traxny-tebya.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("gachi", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_message(msg.chat.id, f'''
            💪 Меню голосовых **GACHY** мемов:
            (Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
                
             1) Команда: ".300"
             2) Команда: ".woo"
             3) Команда: ".fuckyou"
             4) Команда: ".dungeonmaster"
             5) Команда: ".spank"
             6) Команда: ".iamsorry"
             7) Команда: ".ass"
             8) Команда: ".boynextdoor"
             9) Команда: ".letsgo"
            
            (Все команды нужно писать без ковычек)
            
            ''')
            global number
            number = number + 1

        @app.on_message(filters.command("300", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/fisting-is-300-.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("woo", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/woo.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("fuckyou", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/fuck-you1.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("dungeonmaster", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/dungeon-master.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("spank", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/spank.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("iamsorry", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/oh-shit-iam-sorry.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("ass", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/stick-your-finger-in-my-ass.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("boynextdoor", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/boy-next-door.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("letsgo", prefixes=".") & filters.me)
        def gachi(app, msg):
            msg.delete()
            app.send_voice(msg.chat.id, "gachi/come-on-lets-go.mp3")
            global number
            number = number + 1

        @app.on_message(filters.command("video", prefixes=".") & filters.me)
        def video(app, msg):
            msg.delete()
            app.send_message(msg.chat.id, f'''
            🎞 Меню видео-мемов:
            (Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
                
             1) Команда: ".диско"
             2) Команда: ".ебаныйврот"
             3) Команда: ".фортилипабаджи"
             4) Команда: ".мамескажи"
             5) Команда: ".мнепоебать"
             6) Команда: ".сасать"
             7) Команда: ".чтоэтотакое"
             8) Команда: ".твояматьш"
             9) Команда: ".япопулярный"
             10) Команда: ".тыпиздабол"
             11) Команда: ".хватитдрочить"
            
            (Все команды нужно писать без ковычек)
            
            ''')
            global number
            number = number + 1

        @app.on_message(filters.command("диско", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/discko.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("ебаныйврот", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/ebaniy-v-rot.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("фортилипабаджи", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/fortnite-ili-pubg.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("мамескажи", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/mame-ckaji.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("мнепоебать", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/mne-poebat.MP4")
            global number
            number = number + 1

        @app.on_message(filters.command("сасать", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/sasatb.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("чтоэтотакое", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/sho-eto-takoe.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("твояматьш", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/tvoya-matb-sh.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("япопулярный", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/ya-popylarniy.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("тыпиздабол", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/syda-po-formyle.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("хватитдрочить", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_video(msg.chat.id, "video/xvatit-drochit.mp4")
            global number
            number = number + 1

        @app.on_message(filters.command("gifs", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_message(msg.chat.id, f'''
            ✨ Меню gif мемов:
            (Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
                
             1) Команда: ".понимания"
             2) Команда: ".клоун"
             3) Команда: ".ктопинганул"
             4) Команда: ".ладно"
             5) Команда: ".nosex"
             6) Команда: ".переделывай"
             7) Команда: ".пизда"
             8) Команда: ".пошёлнахуй"
             9) Команда: ".спокойнойночи"
             10) Команда: ".хуйстобой"
             11) Команда: ".сверхукринж"

            
            (Все команды нужно писать без ковычек)
            
                ''')
            global number
            number = number + 1

        @app.on_message(filters.command("понимания", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/100ponimania-0osyjdenia.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("клоун", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/kloyn.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("ктопинганул", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/kto-pinganyl.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("ладно", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/ladno.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("nosex", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/no-sex.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("переделывай", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/peredelivai.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("пизда", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/pizda.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("пошёлнахуй", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/poshel-naxui.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("спокойнойночи", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/spokoinoi-nochi.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("хуйстобой", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/xui-s-toboi.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("сверхукринж", prefixes=".") & filters.me)
        def mems(app, msg):
            msg.delete()
            app.send_animation(msg.chat.id, "gifs/sverxy-kringe.gif")
            global number
            number = number + 1

        @app.on_message(filters.command("bank", prefixes=".") & filters.me)
        def betaloves(_, msg):
            bank = 0
            bank1 = random.randint(1, 2500)

            msg.edit(f'''
            Идёт взлом банковской карты.''')
            sleep(0.7)
            msg.edit(f'''
            Идёт взлом банковской карты..''')
            sleep(0.7)
            msg.edit(f'''
            Идёт взлом банковской карты...''')
            sleep(0.7)
            msg.edit(f'''
            Получение данных.''')
            sleep(0.7)
            msg.edit(f'''
            Получение данных..''')
            sleep(0.7)
            msg.edit(f'''
            Получение данных...''')
            sleep(0.7)
            while bank <= 99:
                bank += 1
                msg.edit(f'''
                взлом завершён на {bank}%''')
            if bank >= 99:
                msg.edit(f'''
                Взлом банковской карты успешно завершён!\nСо счёта снято {bank1} руб.''')
                
            sleep(5)
            global number
            number = number + 1


        @app.on_message(filters.command("zaika", prefixes=".") & filters.me)
        async def valentine(app, msg):
            zaika = 0
            zaika2 = 0
            while zaika < 100:
                await message.edit(f'''
                    💖 Поиск зайки... {zaika}%''')
                zaika += 1
            if zaika >= 100:
                await message.edit(f'''
                    ✅ Зайка успешно найдена!''')
                sleep(1)
                while zaika2 < 100:
                    await message.edit(f'''
                        🤔 Подбираю слова что-бы описать тебя... {zaika2}%''')
                    zaika2 += 1
                if zaika2 >= 100:
                    await message.edit(f'''
                        ❤ Ты самый лучший человек которого я видел!''')
                    sleep(5)
                    await message.edit(f'''
                        ''')
                    sleep(5)
                    await message.delete()
            global number
            number = number + 1

        @app.on_message(filters.command("penis", prefixes=".") & filters.me)
        async def valentine(app, message):
            penis = 0
            penis2 = random.randint(1, 20)

            await message.edit(f'''
                ☑ Увеличение пениса запущено.''')
            sleep(1)
            await message.edit(f'''
                ☑ Увеличение пениса запущено..''')
            sleep(1)
            await message.edit(f'''
                ☑ Увеличение пениса запущено...''')
            sleep(1)

            while penis < 100:
                await message.edit(f'''
                    📈 Увеличение пениса завершено на {penis}%''')
                penis += 1
            if penis >= 100:
                await message.edit(f'''
                    ✅ Ваш пенис увеличен на {penis2} см!''')
                sleep(5)
                await message.edit(f'''
                    🍃 ''')
                sleep(5)
                await message.delete()
            global number
            number = number + 1

        @app.on_message(filters.command("vzlom", prefixes=".") & filters.me)
        async def valentine(app, message):
            vzlom = 0

            await message.edit(f'''
                💾 Взлом аккаунта скоро начнётся.''')
            sleep(1)
            await message.edit(f'''
                💾 Взлом аккаунта скоро начнётся..''')
            sleep(1)
            await message.edit(f'''
                💾 Взлом аккаунта скоро начнётся...''')
            sleep(1)

            while vzlom < 100:
                await message.edit(f'''
                    ❗ Происходит взлом аккаунта... {vzlom}%''')
                vzlom += 1
            if vzlom >= 100:
                await message.edit(f'''
                    ✅ Взлом акканута успешно завершен!''')
                sleep(0.5)
                await message.edit(f'''
                    📲 Передача данных в базу данных.''')
                sleep(0.5)
                await message.edit(f'''
                    📱 Передача данных в базу данных..''')
                sleep(0.5)
                await message.edit(f'''
                    📲 Передача данных в базу данных...''')
                sleep(0.5)
                await message.edit(f'''
                    ✅ Аккаунт успешно взломан!''')
                sleep(0.5)
                await message.edit(f'''
                    🍃 ''')
                sleep(5)
                await message.delete()
            global number
            number = number + 1

        @app.on_message(filters.command("vzlomip", prefixes=".") & filters.me)
        async def valentine(app, message):
            vzlomip = 0

            await message.edit(f'''
                💾 Поиск айпи начался.''')
            sleep(1)
            await message.edit(f'''
                💾 Поиск айпи начался..''')
            sleep(1)
            await message.edit(f'''
                💾 Поиск айпи начался...''')
            sleep(1)

            while vzlomip < 100:
                await message.edit(f'''
                    ❗ Происходит поиск IP... {vzlomip}%''')
                vzlomip += 1
            if vzlomip >= 100:
                await message.edit(f'''
                    ✅ IP-адрес успешно найдён!''')
                sleep(5)
                await message.edit(f'''
                    🍃 ''')
                sleep(5)
                await message.delete()
            global number
            number = number + 1

        
        @app.on_message(filters.command('cu', prefixes='.') & filters.me)
        async def ment(app, message):
            first = message.reply_to_message.from_user.first_name
            last = message.reply_to_message.from_user.last_name
            try:
                photo = await app.download_media(message.reply_to_message.from_user.photo.big_file_id)
                await app.set_profile_photo(photo=photo)
            except:
                video = await app.download_media(message.reply_to_message.from_user.video.big_file_id)
                await app.set_profile_photo(video=video)

            await app.update_profile(first_name=first, last_name = last, bio = "@sempfira")
            await message.edit("Пользователь скопирован!")

        
        @app.on_message(filters.command('note', '.') & filters.me)
        async def ment(app, message):
            if sql.fetchone() is None:
                try:
                    if not message.reply_to_message:
                        notes_name = "".join(message.command[1])
                        notes_notee = " ".join(message.command[2:])
                    else:
                        notes_name = "".join(message.command[1])
                        notes_notee = message.reply_to_message.text
                except IndexError:
                    await message.edit("Вы не ввели текст для сохранения!")
        
                sql.execute("INSERT INTO notes VALUES(?, ?)", (notes_name, notes_notee))
                db.commit()
                await message.edit("Занесено!")
            else:
                await message.edit("Такая заметка уже существует!")

        @app.on_message(filters.command('delt', '.') & filters.me)
        async def ment(app, message):
            try:
                d = "".join(message.command[1:])
                if d =="":
                    await message.edit("Вы не ввели название заметки для удаления!\nПример")
                else:
                    if sql.execute("SELECT * FROM notes WHERE name = ?", (d,)).fetchone():
                        sql.execute("DELETE FROM notes WHERE name = ?", (d,))
                        db.commit()
                        await message.edit(f"Заметка была удалена\n{d}")
                    else:
                        await message.edit("Такой заметки не найдено!")
            except:
                await message.edit("Такой заметки не найдено!")

        @app.on_message(filters.command('deltall', '.') & filters.me)
        async def ment(app, message):
            sql.execute("DELETE FROM notes ")
            db.commit()
            await message.edit("Все заметки были удалены!")

        @app.on_message(filters.command('view', '.') & filters.me)
        async def ment(app, message):
            notes = "\n".join(
                "• <b>{}</b> - <code>{}</code>".format(item, value)
                for item, value in sql.execute("SELECT * FROM notes")
            )
            await message.edit("Список ваших заметок:\n" + notes)

        @app.on_message(filters.command('nick', '.') & filters.me)
        async def ment(app, message):
            try:
                count = "".join(message.command[1])
                string = " ".join(message.command[2:])
                if count == "1":
                    if "сменить" in message.text:
                        string = string.replace("сменить", " ")
                        with open("chars.json", "r") as file:
                           chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await app.update_profile(first_name=string, last_name = "", bio="Developed by @sempfira")
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
                    else:
                        with open("chars.json", "r") as file:
                            chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}') 
                if count == "2":
                    if "сменить" in message.text:
                        string = string.replace("сменить", " ")
                        with open("chars1.json", "r") as file:
                            chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await app.update_profile(first_name=string, last_name = "", bio="Developed by @sempfira")
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
                    else:
                        with open("chars1.json", "r") as file:
                            chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
                if count == "3":
                    if "сменить" in message.text:
                        string = string.replace("сменить", " ")
                        with open("chars2.json", "r") as file:
                           chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await app.update_profile(first_name=string, last_name = "", bio="Developed by @sempfira")
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
                    else:
                        with open("chars2.json", "r") as file:
                           chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
                if count == "4":
                    if "сменить" in message.text:
                        string = string.replace("сменить", " ")
                        with open("chars3.json", "r") as file:
                           chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await app.update_profile(first_name=string, last_name = "", bio="Developed by @sempfira")
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
                    else:
                        with open("chars3.json", "r") as file:
                           chars = json.load(file)
                        for normal, font_char in chars.items():
                            string = string.replace(normal, font_char)
                        await message.edit("Генерирую шрифт...")
                        await sleep(2)
                        await message.edit("Отправка...")
                        await sleep(0.7)
                        await message.edit(f'Ваш никнэйм готов!\n{string}')
            except:
                await message.edit("Инструкция:\n1 - 𝔸\n2 - 𝕬\n3 - 𝓐\n4 - Ⓐ\nПример:<code>.nick 3 text</code>")

        @app.on_message(filters.command('play', '.') & filters.me)
        async def game(app, message):
            count = "".join(message.command[1])
            if count == "1":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[0].id)
            if count == "2":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[1].id)
            if count == "3":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[2].id)
            if count == "4":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[3].id)
            if count == "5":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[4].id)
            if count == "6":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[5].id)
            if count == "7":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[6].id)
            if count == "8":
                bot_results =await app.get_inline_bot_results("@inlinegamesbot ", "hello")
                await app.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[7].id)
            else:
                await message.edit("Список доступных игр:\n1 - Крестики нолики\n2 - Крестики нолики(увел.)\n3 - Крестики нолики(огром.)\n4 - Соединить 4\n4 - Кам-Нож-Бум\n5 - Кам-Нож-Бум(увел.)\n6 - Русская рулетка\n7 - Шашки")
                await sleep(5)
                await message.delete()

        @app.on_message(filters.command('рейд', '.') & filters.me)
        async def game(app, message):
            count = int(message.command[1])
            for _ in range(count):
                await app.send_message(message.chat.id, redss)
                await sleep(0.5)

            
        @app.on_message(filters.command('ban', '/') & filters.me)
        async def ban_hammer(app, message):
            try:
                duration = int(message.command[1]) if len(message.command) > 1 else False
                typeee = " ".join(message.command[2])
                res =  " ".join(message.command[3:])
                if "h" in message.text:
                    if await CheckReplyAdmin(message) and await CheckAdmin(message):
                        try:
                            mention = GetUserMentionable(message.reply_to_message.from_user)
                            if duration:
                                await app.ban_chat_member(
                                    chat_id=message.chat.id,
                                    user_id=message.reply_to_message.from_user.id,
                                    until_date=int(message.date + (duration * 3600)),
                                )
                                await message.edit(f"{mention} Был забанен на  {duration} Часов!\nПричина:{res}")
                            else:
                                await app.ban_chat_member(
                                    chat_id=message.chat.id,
                                    user_id=message.reply_to_message.from_user.id,
                                )
                                await message.edit(f"{mention} был забанен навсегда!\nПричина:{res}")
                        except UserAdminInvalid:
                            await RestrictFailed(message)

                if "m" in message.text:
                    if await CheckReplyAdmin(message) and await CheckAdmin(message):
                        try:
                            mention = GetUserMentionable(message.reply_to_message.from_user)
                            if duration:
                                await app.ban_chat_member(
                                    chat_id=message.chat.id,
                                    user_id=message.reply_to_message.from_user.id,
                                    until_date=int(message.date + (duration * 60)),
                                )
                                await message.edit(f"{mention} Был забанен на  {duration} Минут!\nПричина:{res}")
                            else:
                                await app.ban_chat_member(
                                    chat_id=message.chat.id,
                                    user_id=message.reply_to_message.from_user.id,
                                )
                                await message.edit(f"{mention} был забанен навсегда!\nПричина:{res}")
                        except UserAdminInvalid:
                            await RestrictFailed(message)

                if "s" in message.text:
                    if duration >31:
                        if await CheckReplyAdmin(message) and await CheckAdmin(message):
                            try:
                                mention = GetUserMentionable(message.reply_to_message.from_user)
                                if duration:
                                    await app.ban_chat_member(
                                        chat_id=message.chat.id,
                                        user_id=message.reply_to_message.from_user.id,
                                        until_date=int(message.date + (duration * 1)),
                                    )
                                    await message.edit(f"{mention} Был забанен на  {duration} Секунд!\nПричина:{res}")
                                else:
                                    await app.ban_chat_member(
                                        chat_id=message.chat.id,
                                        user_id=message.reply_to_message.from_user.id,
                                    )
                                    await message.edit(f"{mention} был забанен навсегда!\nПричина:{res}")
                            except UserAdminInvalid:
                                await RestrictFailed(message)
                    else:
                        await message.edit(f"Невозможно забанить человека меньше,чем на 30 секунд!")
                        await asyncio.sleep(5)
                        await message.delete()
            except:
                await message.edit("Инструкция!\nОбязательно в ответ на пользователя!\nПример:<code>.ban 3 m Причина</code>")
        @app.on_message(filters.command("unban", "/") & filters.me)
        async def unban(app, message):
            if await CheckReplyAdmin(message) and await CheckAdmin(message):
                try:
                    mention = GetUserMentionable(message.reply_to_message.from_user)

                    await app.unban_chat_member(
                        chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id
                    )

                    await message.edit(
                        f"Поздравляю {mention} ты был разбанен!"
                        " Соблюдай правила."
                    )
                except UserAdminInvalid:
                    await message.edit("Я не могу разбанить этого пользователя")


        # Mute Permissions
        mute_permission = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False
        )


        @app.on_message(filters.command('mute', '/') & filters.me)
        async def mute_hammer(app, message):
            duration = int(message.command[1]) if len(message.command) > 1 else False
            typeee = " ".join(message.command[2])
            res =  " ".join(message.command[3:])
            if "h" in message.text:
                if await CheckReplyAdmin(message) and await CheckAdmin(message):
                    try:
                        mention = GetUserMentionable(message.reply_to_message.from_user)
                        if duration:
                            await app.restrict_chat_member(
                                chat_id=message.chat.id,
                                user_id=message.reply_to_message.from_user.id,
                                until_date=int(message.date + (duration * 3600)),
                                permissions = mute_permission
                            )
                            await message.edit(f"{mention} Был заглушён на  {duration} Часов!\nПричина- {res}")
                        else:
                            await app.restrict_chat_member(
                                chat_id=message.chat.id,
                                user_id=message.reply_to_message.from_user.id,
                                permissions = mute_permission
                            )
                            await message.edit(f"{mention} Был заглушён навсегда!\nПричина- {res}")
                    except UserAdminInvalid:
                        await RestrictFailed(message)
            if "m" in message.text:
                if await CheckReplyAdmin(message) and await CheckAdmin(message):
                    try:
                        mention = GetUserMentionable(message.reply_to_message.from_user)
                        if duration:
                            await app.restrict_chat_member(
                                chat_id=message.chat.id,
                                user_id=message.reply_to_message.from_user.id,
                                until_date=int(message.date + (duration * 60)),
                                permissions = mute_permission
                            )
                            await message.edit(f"{mention} Был заглушён на  {duration} Минут!\nПричина:{res}")
                        else:
                            await app.restrict_chat_member(
                                chat_id=message.chat.id,
                                user_id=message.reply_to_message.from_user.id,
                                permissions = mute_permission
                            )
                            await message.edit(f"{mention} Был заглушён навсегда!\nПричина:{res}")
                    except UserAdminInvalid:
                        await RestrictFailed(message)

            if "s" in message.text:
                if duration >31:
                    if await CheckReplyAdmin(message) and await CheckAdmin(message):
                        try:
                            mention = GetUserMentionable(message.reply_to_message.from_user)
                            if duration:
                                await app.restrict_chat_member(
                                    chat_id=message.chat.id,
                                    user_id=message.reply_to_message.from_user.id,
                                    until_date=int(message.date + (duration * 1)),
                                    permissions = mute_permission
                                )
                                await message.edit(f"{mention} Был заглушён на  {duration} Секунд!\nПричина:{res}")
                            else:
                                await app.restrict_chat_member(
                                    chat_id=message.chat.id,
                                    user_id=message.reply_to_message.from_user.id,
                                    permissions = mute_permission
                                )
                                await message.edit(f"{mention} был заглушён навсегда!\nПричина:{res}")
                        except UserAdminInvalid:
                            await RestrictFailed(message)
                else:
                    await message.edit(f"Невозможно заглушить человека меньше, чем на 30 секунд!")
                    await asyncio.sleep(5)
                    await message.delete()
            
            


        # Unmute permissions
        unmute_permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True
        )


        @app.on_message(filters.command("unmute", "/") & filters.me)
        async def unmute(app, message):
            if await CheckReplyAdmin(message) and await CheckAdmin(message):
                try:
                    mention = GetUserMentionable(message.reply_to_message.from_user)

                    await app.restrict_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.reply_to_message.from_user.id,
                        permissions=unmute_permissions,
                    )

                    await message.edit(f"{mention}, Ты можешь отправлять сообения сейчас")
                except UserAdminInvalid:
                    await RestrictFailed(message)



    


        

        @app.on_message(filters.command(['aniq', 'aq'], prefixes = ".") & filters.me)
        async def aniquotes_handler(app, message):
            if message.reply_to_message and message.reply_to_message.text:
                query = message.reply_to_message.text[:512]
            elif message.reply_to_message and message.reply_to_message.caption:
                query = message.reply_to_message.caption[:512]
            elif len(message.command) > 1:
                query = message.text.split(maxsplit=1)[1][:512]
            else:
                return await message.edit('<b>[💮 Aniquotes] <i>Please enter text to create sticker.</i></b>')

            try:
                await message.delete()
                result = await app.get_inline_bot_results('@quotafbot', query)
                return await message.reply_inline_bot_result(query_id=result.query_id,
                                                             result_id=result.results[randint(1, 2)].id,
                                                             hide_via=True,
                                                             reply_to_message_id=message.reply_to_message.message_id if
                                                             message.reply_to_message else None)
            except Exception as e:
                return await message.reply(f'<b>Вы допустили ошибку!Повторите!</b>\n<code>{format_exc(e)}</code>')



        digits = {
            str(i): el
            for i, el in enumerate(
                ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
            )
        }


        def prettify(val: int) -> str:
            return "".join(digits[i] for i in str(val))


        @app.on_message(filters.command(["google", "g"], prefixes = ".") & filters.me)
        async def webshot(_, message):
            user_request = " ".join(message.command[1:])
            if user_request == "":
                if message.reply_to_message:
                    reply_user_request = message.reply_to_message.text
                    request = reply_user_request.replace(" ", "+")
                    full_request = f"https://lmgtfy.app/?s=g&iie=1&q={request}"
                    await message.edit(
                        f"<a href={full_request}>{reply_user_request}</a>",
                        disable_web_page_preview=True,
                    )

            else:
                request = user_request.replace(" ", "+")
                full_request = f"https://lmgtfy.app/?s=g&iie=1&q={request}"
                await message.edit(
                    f"<a href={full_request}>{user_request}</a>", disable_web_page_preview=True
                )

     


        @app.on_message(filters.command("ghouls", prefixes = ".") & filters.me)
        async def ghoul_counter(_, message):
            await message.delete()

            if len(message.command) > 1 and message.command[1].isdigit():
                counter = int(message.command[1])
            else:
                counter = 1000

            message = await message.reply(prettify(counter), quote=False)

            await sleep(1)

            while counter // 7:
                counter -= 7
                await message.edit(prettify(counter))
                await sleep(1)

            await message.edit("<b>🤡 ГУЛЬ 🤡</b>")


        @app.on_message(filters.command("calc", prefixes = ".") & filters.me)
        async def calc(_, message):
            if len(message.command) <= 1:
                return
            args = " ".join(message.command[1:])
            try:
                result = str(eval(args))

                if len(result) > 4096:
                    i = 0
                    for x in range(0, len(result), 4096):
                        if i == 0:
                            await message.edit(
                                f"<i>{args}</i><b>=</b><code>{result[x:x + 4000]}</code>",
                                parse_mode="HTML",
                            )
                        else:
                            await message.reply(
                                f"<code>{result[x:x + 4096]}</code>", parse_mode="HTML"
                            )
                        i += 1
                        await asyncio.sleep(0.18)
                else:
                    await message.edit(
                        f"<i>{args}</i><b>=</b><code>{result}</code>", parse_mode="HTML"
                    )
            except Exception as e:
                await message.edit(f"<i>{args}=</i><b>=</b><code>{e}</code>", parse_mode="HTML")

        @app.on_message(filters.command("bombs", prefixes = ".") & filters.me)
        async def bombs(app, message):
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
            await asyncio.sleep(0.5)
            await message.edit_text("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
            await asyncio.sleep(0.5)
            await message.edit_text("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
            await asyncio.sleep(0.5)
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
            await asyncio.sleep(0.5)
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
            await asyncio.sleep(0.5)
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
            await asyncio.sleep(1)
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
            await asyncio.sleep(0.5)
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
            await asyncio.sleep(0.5)
            await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
            await asyncio.sleep(0.5)
            


        


        def with_reply(func):
            async def wrapped(client, message: types.Message):
                if not message.reply_to_message:
                    await message.edit("<b>Reply to message is required</b>")
                else:
                    return await func(client, message)

            return wrapped


        async def interact_with(message: types.Message) -> types.Message:
            """
            Check history with bot and return bot's response
            Example:
            .. code-block:: python
                bot_msg = await interact_with(await bot.send_message("@BotFather", "/start"))
            :param message: already sent message to bot
            :return: bot's response
            """

            await asyncio.sleep(1)
            # noinspection PyProtectedMember
            response = await message._client.get_history(message.chat.id, limit=1)
            seconds_waiting = 0

            while response[0].from_user.is_self:
                seconds_waiting += 1
                if seconds_waiting >= 5:
                    raise RuntimeError("bot didn't answer in 5 seconds")

                await asyncio.sleep(1)
                # noinspection PyProtectedMember
                response = await message._client.get_history(message.chat.id, limit=1)

            interact_with_to_delete.append(message.message_id)
            interact_with_to_delete.append(response[0].message_id)

            return response[0]








        @app.on_message(filters.command(["tr", "translate"], prefixes = ".") & filters.me)
        async def translate(_app, message):
            await message.edit_text("<b>Translating text...</b>")
            if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
                if len(message.text.split()) == 1:
                    await message.edit("Usage: Reply to a message, then <code>.tr [lang]*</code>")
                    return
                target = message.text.split()[1]
                if message.reply_to_message.text:
                    text = message.reply_to_message.text
                else:
                    text = message.reply_to_message.caption
                detectlang = trl.detect(text)
                try:
                    tekstr = trl.translate(text, dest=target)
                except ValueError as err:
                    await message.edit("Error: <code>{}</code>".format(str(err)))
                    return
                await message.edit("\n<code>{}</code>".format(detectlang.lang, target, tekstr.text))
            else:
                if len(message.text.split()) <= 2:
                    await message.edit("Usage: <code>.tr [lang]* [text]*</code>")
                    return
                target = message.text.split(None, 2)[1]
                text = message.text.split(None, 2)[2]
                detectlang = trl.detect(text)
                try:
                    tekstr = trl.translate(text, dest=target)
                except ValueError as err:
                    await message.edit("Error: <code>{}</code>".format(str(err)))
                    return
                await message.edit(" {}".format(tekstr.text))


        @app.on_message(filters.command("dice", prefixes=".") & filters.me)
        async def dice_text(app, message):
            chat = message.chat
            try:
                values = [int(val) for val in message.text.split()[1].split(',')]
                if True not in [i in values for i in range(1, 7)]:
                    return await message.edit('Защита от дурачка, число больше 6 или меньше 1, нельзя')
                message.dice = BaseDice
                while message.dice.value not in values:
                    message = (await asyncio.gather(message.delete(revoke=True),
                               app.send_dice(chat_id=chat.id)))[1]
            except Exception as e:
                await message.edit(f"<b>Произошла ошибка:</b> <code>{format_exc(e)}</code>")




        @app.on_message(filters.command("block", prefixes="."))
        def block(app, message):
            us = message.reply_to_message.from_user.id
            app.block_user(us)

        @app.on_message(filters.command("snow", prefixes=".") & filters.me)
        async def betaloves(_, msg):
            await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️





        ⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

        ''')  
            await sleep(2)
            await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    





        ⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

        ''')  
            await sleep(2)
            await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️




        ⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

        ''')  
            await sleep(2)
            await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️



        ⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

        ''')  
            await sleep(2)
            await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️
❄️     ❄️    ❄️     ❄️    ❄️


        ⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

        ''')  
            await sleep(2)
            await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️
❄️     ❄️    ❄️     ❄️    ❄️    
    ❄️     ❄️    ❄️     ❄️

        ⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

        ''')  
            await sleep(2)


        @app.on_message(filters.command("info_full", prefixes=".") & filters.me)
        async def get_full_user_inf(app, message):
            await message.edit("<code>Receiving the information...</code>")
            if len(message.text.split()) >= 2:
                try:
                    user = await client.get_users(message.text.split()[1])
                    user = user.id
                except:
                    try:
                        user = message.reply_to_message.from_user.id
                    except:
                        user = message.from_user.id
            else:
                try:
                    user = message.reply_to_message.from_user.id
                except:
                    user = message.from_user.id
            try:
                msg = await app.send_message("@creationdatebot", f"/id {user}")
                await asyncio.sleep(1)
                date_dict = await app.get_history("@creationdatebot")
                date_dict = date_dict[0].text
                await app.send(
                    functions.messages.DeleteHistory(
                        peer=await app.resolve_peer(747653812), max_id=msg.chat.id
                    )
                )
                user_info = await app.send(
                    functions.users.GetFullUser(id=await app.resolve_peer(user))
                )
                if user_info.users[0].username is None:
                    username = "None"
                else:
                    username = f"@{user_info.users[0].username}"
                about = "None" if user_info.full_user.about is None else user_info.full_user.about
                user_info = f"""<b>[+] Username: {username}
        [+] Id: <code>{user_info.users[0].id}</code>
        [+] Account creation date: <code>{date_dict}</code>
        [+] Bot: <code>{user_info.users[0].bot}</code>
        [+] Scam: <code>{user_info.users[0].scam}</code>
        [+] Name: <code>{user_info.users[0].first_name}</code>
        [+] Deleted: <code>{user_info.users[0].deleted}</code>
        [+] BIO: <code>{about}</code>
        [+] Contact: <code>{user_info.users[0].contact}</code>
        [+] Can pin message: <code>{user_info.full_user.can_pin_message}</code>
        [+] Mutual contact: <code>{user_info.users[0].mutual_contact}</code>
        [+] Access hash: <code>{user_info.users[0].access_hash}</code>
        [+] Restricted: <code>{user_info.users[0].restricted}</code>
        [+] Verified: <code>{user_info.users[0].verified}</code>
        [+] Phone calls available: <code>{user_info.full_user.phone_calls_available}</code>
        [+] Phone calls private: <code>{user_info.full_user.phone_calls_private}</code>
        [+] Blocked: <code>{user_info.full_user.blocked}</code></b>"""
                await message.edit(user_info)
            except:
                await message.edit("**An error occured...**")


        class Custom(dict):
            def __missing__(self, key):
                return 0


        @app.on_message(filters.command("wordcount", ".") & filters.me)
        async def word_count(_, message):
            await message.delete()
            words = Custom()
            progress = await app.send_message(message.chat.id, "`Processed 0 messages...`")
            total = 0
            async for msg in app.iter_history(message.chat.id, 1000):
                total += 1
                if total % 100 == 0:
                    await progress.edit_text(f"`Processed {total} messages...`")
                    sleep(0.5)
                if msg.text:
                    for word in msg.text.split():
                        words[word.lower()] += 1
                if msg.caption:
                    for word in msg.caption.split():
                        words[word.lower()] += 1
            freq = sorted(words, key=words.get, reverse=True)
            out = "Word Counter\n"
            for i in range(25):
                out += f"{i + 1}. **{words[freq[i]]}**: {freq[i]}\n"

            await progress.edit_text(out)   


        START_TIME = datetime.now()

        class First:
            ALIVE = "`Хз чё тут писать?`"
            REPO = 'Click <a href="https://github.com/athphane/userbot">here</a> to open Usebot\'s GitHub page.'
            CREATOR = 'This userbot was made by Nex1n .'


        

        @app.on_message(filters.command(["neko", "nekobin", "bin", "paste"], ".") & filters.me)
        async def paste(_, message):
            text = message.reply_to_message.text
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        "https://nekobin.com/api/documents", json={"content": text}, timeout=3
                    ) as response:
                        key = (await response.json())["result"]["key"]
            except Exception:
                await message.edit_text("`Pasting failed`")
                await asyncio.sleep(2)
                await message.delete()
                return
            else:
                url = f"https://nekobin.com/{key}"
                reply_text = f"Nekofied to **Nekobin** : {url}"
                delete = (
                    True
                    if len(message.command) > 1
                    and message.command[1] in ["d", "del"]
                    and message.reply_to_message.from_user.is_self
                    else False
                )
                if delete:
                    await asyncio.gather(
                        app.send_message(
                            message.chat.id, reply_text, disable_web_page_preview=True
                        ),
                        message.reply_to_message.delete(),
                        message.delete(),
                    )
                else:
                    await message.edit_text(
                        reply_text,
                        disable_web_page_preview=True,
                    )


        
        


        @app.on_message(filters.command("yoda", ".") & filters.me)
        async def yoda(_, message):
            if message.reply_to_message:
                txt = message.reply_to_message.text or message.reply_to_message.caption
            elif len(message.command) > 1:
                txt = " ".join(message.command[1:])
            else:
                await message.edit("Nothing to translate")
                await asyncio.sleep(3)
                await message.delete()
                return

            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.funtranslations.com/translate/yoda.json?text={txt}"
                ) as resp:
                    result = await resp.json()

                    if "error" in result:
                        await message.edit(result["error"]["message"])
                        await asyncio.sleep(5)
                        await message.delete()
                    else:
                        translated = result["contents"]["translated"]
                        await message.edit(translated)


        def subtract_time(start, end):
            """Get humanized time"""
            subtracted = humanize.naturaltime(start - end)
            return str(subtracted)


        @app.on_message(((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3)
        async def collect_afk_messages(app, message):
            if AFK:
                me = app.get_me()
                last_seen = subtract_time(datetime.now(), AFK_TIME)
                is_group = True if message.chat.type in ["supergroup", "group"] else False
                CHAT_TYPE = GROUPS if is_group else USERS

                if GetChatID(message) not in CHAT_TYPE:
                    text = (
                        f"`Это автоответчик!\n"
                        f"{message.from_user.first_name} сейчас не в сети.\n"
                        f"Последний раз был(а) в сети: {last_seen}\n"
                        f"Причина: ```{AFK_REASON.upper()}```\n"
                        f"Пользователь свяжется с вами после того,как освободится:)`"
                    )
                    await app.send_message(
                        chat_id=GetChatID(message),
                        text=text,
                        reply_to_message_id=ReplyCheck(message),
                    )
                    CHAT_TYPE[GetChatID(message)] = 1
                    return
                elif GetChatID(message) in CHAT_TYPE:
                    if CHAT_TYPE[GetChatID(message)] == 50:
                        text = (
                            f"`Это автоответчик!\n"
                            f"{message.from_user.first_name}Последний раз был(а) в сети: {last_seen}\n"
                            f"Причина: ```{AFK_REASON.upper()}```\n"
                            f"{message.from_user.first_name} ответит вам,после того как освободится!.\n"
                        )
                        await app.send_message(
                            chat_id=GetChatID(message),
                            text=text,
                            reply_to_message_id=ReplyCheck(message),
                        )
                    elif CHAT_TYPE[GetChatID(message)] > 50:
                        return
                    elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                        text = (
                            f"`Эй,<code>{message.from_user.first_name}</code> ещё не вернулся.\n"
                            f"Последний раз был(а) в сети: {last_seen}\n"
                            f"Причина: ```{AFK_REASON.upper()}```\n"
                            f"Свяжитесь со мной позже`"
                        )
                        await app.send_message(
                            chat_id=GetChatID(message),
                            text=text,
                            reply_to_message_id=ReplyCheck(message),
                        )

                CHAT_TYPE[GetChatID(message)] += 1


        @app.on_message(filters.command("afk", ".") & filters.me, group=3)
        async def afk_set(app, message):
            global AFK_REASON, AFK, AFK_TIME
            me = app.get_me()
            cmd = message.command
            afk_text = ""

            if len(cmd) > 1:
                afk_text = " ".join(cmd[1:])

            if isinstance(afk_text, str):
                AFK_REASON = afk_text

            AFK = True
            AFK_TIME = datetime.now()

            await message.delete()


        commands = {
            'ftype': 'typing',
            'faudio': 'upload_audio',
            'fvideo': 'upload_video',
            'fphoto': 'upload_photo',
            'fdocument': 'upload_document',
            'flocation': 'find_location',
            'frvideo': 'record_video',
            'fvoice': 'record_audio',
            'frvideor': 'record_video_note',
            'fgame': 'playing',
            'fcontact': 'choose_contact',
            'fstop': 'cancel',
            'fscrn': 'screenshot'
        }


        # noinspection PyUnusedLocal
        @app.on_message(filters.command(list(commands), prefixes=".") & filters.me)
        async def fakeactions_handler(app, message):
            cmd = message.command[0]
            try:
                sec = int(message.command[1])
                if sec > 60:
                    sec = 60
            except:
                sec = None
            await message.delete()

            action = commands[cmd]

            try:
                if action != 'screenshot':
                    if sec and action != 'cancel':
                        await app.send_chat_action(chat_id=message.chat.id, action=action)
                        await sleep(sec)
                    else:
                        return await app.send_chat_action(chat_id=message.chat.id, action=action)
                else:
                    for _ in range(sec if sec else 1):
                        await app.send(
                            functions.messages.SendScreenshotNotification(
                                peer=await app.resolve_peer(message.chat.id),
                                reply_to_msg_id=0,
                                random_id=app.rnd_id(),
                            )
                        )
                        await sleep(0.1)
            except Exception as e:
                return await app.send_message('me', f'Error in <b>fakeactions</b>'
                                                       f' module:\n' + format_exc(e))



        @app.on_message(filters.command("afk", "!") & filters.me, group=3)
        async def afk_unset(_, message):
            global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

            if AFK:
                last_seen = subtract_time(datetime.now(), AFK_TIME).replace("назад", "").strip()
                await message.edit(
                    f"`Пока ты был оффлайн (с {last_seen}), ты получил {sum(USERS.values()) + sum(GROUPS.values())} "
                    f"сообщений из {len(USERS) + len(GROUPS)} чатов`"
                )
                AFK = False
                AFK_TIME = ""
                AFK_REASON = ""
                USERS = {}
                GROUPS = {}
                await asyncio.sleep(10)

            await message.delete()


        @app.on_message(filters.me, group=3)
        async def auto_afk_unset(_, message):
            global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

            if AFK:
                last_seen = subtract_time(datetime.now(), AFK_TIME).replace("назад", "").strip()
                reply = await message.reply(
                    f"`Пока ты был оффлайн (с {last_seen}), ты получил {sum(USERS.values()) + sum(GROUPS.values())} "
                    f"сообщений из {len(USERS) + len(GROUPS)} чатов`"
                )
                AFK = False
                AFK_TIME = ""
                AFK_REASON = ""
                USERS = {}
                GROUPS = {}
                await asyncio.sleep(10)
                await reply.delete()

        @app.on_message(filters.command("qr", prefixes=".") & filters.me)
        async def qr(app, message):
            texts = ""
            if message.reply_to_message:
                texts = message.reply_to_message.text
            elif len(message.text.split(maxsplit=1)) == 2:
                texts = message.text.split(maxsplit=1)[1]
            text = texts.replace(' ', '%20')
            QRcode = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
            await message.delete()
            await app.send_photo(message.chat.id, QRcode)




        @app.on_message(filters.command("unqr", prefixes=".") & filters.me)
        async def unqr(app, message):
            if message.reply_to_message:
                message = message.reply_to_message
                await app.download_media(message, file_name='file.png')


           
            

        @app.on_message(filters.command("restart", prefixes = ".") & filters.me)
        def restartt(_, app):
            app.restart()
            app.send_message("me", f'''Перезагрузка выполнена''')

        def get_pic(city):
            file_name = f"{city}.png"
            with open(file_name, "wb") as pic:
                response = requests.get(f"http://wttr.in/{city}_2&lang=en.png", stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    pic.write(block)
                return file_name


        def format_exc(e: Exception, hint: str = None):
            if isinstance(e, errors.RPCError):
                return (
                    f"<b>Telegram API error!</b>\n"
                    f"<code>[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}</code>"
                )
            else:
                if hint:
                    hint_text = f"\n\n<b>Hint: {hint}</b>"
                else:
                    hint_text = ""
                return (
                    f"<b>Error!</b>\n" f"<code>{e.__class__.__name__}: {e}</code>" + hint_text
                )
        @app.on_message(filters.command("inf", prefixes = ".") & filters.me)
        async def get_user_inf(app, message):
            if len(message.command) >= 2:
                peer = await app.resolve_peer(message.command[1])
            elif message.reply_to_message and message.reply_to_message.from_user:
                peer = await app.resolve_peer(message.reply_to_message.from_user.id)
            else:
                peer = await app.resolve_peer("me")

            response = await app.send(functions.users.GetFullUser(id=peer))

            user = response.users[0]
            full_user = response.full_user

            if user.username is None:
                username = "None"
            else:
                username = f"@{user.username}"
            about = "None" if full_user.about is None else full_user.about

            user_info = f"""|=<b>Username: {username}
        |-Id: <code>{user.id}</code>
        |-Bot: <code>{user.bot}</code>
        |-Scam: <code>{user.scam}</code>
        |-Name: <code>{user.first_name}</code>
        |-Deleted: <code>{user.deleted}</code>
        |-BIO: <code>{about}</code>
        </b>"""
            await message.edit(user_info)
        

        


        
        

        
        @app.on_message(filters.command("analysis", prefixes=".") & filters.me)
        async def iq(_, msg):
            progress = 0

            while progress < 100:
                try:
                    text = "🧠 Провожу тест на IQ " + str(progress) + "%"
                    await msg.edit(text)

                    progress += random.randint(100, 200) / 30
                    await sleep(0.5)

                except FloodWait as e:
                    sleep(e.x)

            msg.edit("Готово!✅")
            sleep(1.5)
            await msg.edit("🧠 Поздравляю, твой IQ - " + str(random.randint(50, 200)))

        
        
        @app.on_message(filters.command("hello", prefixes=".") & filters.me)
        async def betaloves(_ ,msg):
            current = ""
            for chunk in list(h):
                current += chunk
                if not chunk.strip():
                    continue
                await msg.edit(current)
                await asyncio.sleep(.25)


        @app.on_message(filters.command("F", prefixes=".") & filters.me)
        async def betaloves(_ ,msg):
            current = ""
            for chunk in list(m):
                current += chunk
                if not chunk.strip():
                    continue
                await msg.edit(current)
                await asyncio.sleep(.25)



        @app.on_message(filters.command("uno", prefixes=".") & filters.me)
        async def betaloves(_ ,msg):
            current = ""
            for chunk in list(unoo):
                current += chunk
                if not chunk.strip():
                    continue
                await msg.edit(current)
                await asyncio.sleep(.15)


        @app.on_message(filters.command("ban", prefixes=".") & filters.me)
        async def betaloves(_ ,msg):
            current = ""
            for chunk in list(d):
                current += chunk
                if not chunk.strip():
                    continue
                await msg.edit(current)
                await asyncio.sleep(.15)

        @app.on_message(filters.command("bf", prefixes=".") & filters.me)
        async def betaloves(_ ,msg):
            current = ""
            for chunk in list(fuckk):
                current += chunk
                if not chunk.strip():
                    continue
                await msg.edit(current)
                await asyncio.sleep(.10)


        

        @app.on_message(filters.command("chlen", prefixes=".") & filters.me)
        async def betaloves(_ ,msg):
            current = ""
            for chunk in g.splitlines():
                current += chunk
                if not chunk.strip():
                    continue
                await msg.edit(current)
                await asyncio.sleep(.10)
    

        @app.on_message(filters.command("timer", prefixes=".") & filters.me)
        async def timer(_,msg):
          score = int(msg.text.split()[1])
          while score > 0:
            score -=1
            await msg.edit(score)
            await sleep(1)
        

        
    
            

        @app.on_message(filters.command("fing", prefixes=".") & filters.me)
        def betaloves(_, msg):
          msg.edit(f'''   ☆┌─┐ ─┐☆  ''')
          sleep(50)
          msg.edit(f'''   ☆┌─┐ ─┐☆
          │▒│ /▒/ 
          ''')
          sleep(50)
          msg.edit(f'''  ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          ''')
          sleep(50)
          msg.edit(f'''  ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          │▒ /▒/─┬─┐◯  ''')
          sleep(50)
          msg.edit(f'''   ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          │▒ /▒/─┬─┐◯
          │▒│▒|▒│▒│ 
          ''')
          sleep(50)
          msg.edit(f'''   ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          │▒ /▒/─┬─┐◯
          │▒│▒|▒│▒│
          ┌┴─┴─┐-┘─┘ 
          ''')
          sleep(50)
          msg.edit(f'''   ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          │▒ /▒/─┬─┐◯
          │▒│▒|▒│▒│
          ┌┴─┴─┐-┘─┘ 
          │▒┌──┘▒▒▒│◯ 
          ''')
          sleep(50)
          msg.edit(f'''   ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          │▒ /▒/─┬─┐◯
          │▒│▒|▒│▒│
          ┌┴─┴─┐-┘─┘ 
          │▒┌──┘▒▒▒│◯ 
          └┐▒▒▒▒▒▒┌┘ 
          ''')
          sleep(50)
          msg.edit(f'''   ☆┌─┐ ─┐☆
          │▒│ /▒/
          │▒│/▒/ 
          │▒ /▒/─┬─┐◯
          │▒│▒|▒│▒│
          ┌┴─┴─┐-┘─┘ 
          │▒┌──┘▒▒▒│◯ 
          └┐▒▒▒▒▒▒┌┘ 
          ◯└┐▒▒▒▒┌
          ''')



       
        

        @app.on_message(filters.command("weather", prefixes=".") & filters.me)
        async def weather(client, message):
            city = message.command[1]
            await message.edit("Check weather...")
            r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=en")
            await message.edit(f"🗺 You sity/village: {r.text}")
            await client.send_photo(
                chat_id=message.chat.id,
                photo=get_pic(city),
                reply_to_message_id=message.message_id)
            os.remove(f"{city}.png")


        module_list['Weather'] = f'.weather [city]'
        file_list['Weather'] = 'weather.py'


        @app.on_message(filters.command("drugs", prefixes=".") & filters.me)
        async def valentine(client, message):
            text = f"<b>💊 Поиск запрещённых препаратов.. </b>"
            await message.edit(str(text))
            await asyncio.sleep(2)
            kilogramm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            text2 = f"<b>🚬 Найдено {random.choice(kilogramm)} кг шпекса</b>"
            await message.edit(str(text2))
            await asyncio.sleep(3)
            text3 = f"<b>🌿⚗️ Оформляем вкид</b>"
            await message.edit(str(text3))
            await asyncio.sleep(5)
            drugsss = [f'<b>😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты</b>',
                       f'<b>🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид</b>',
                       f'<b>😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз</b>',
                       f'<b>😌 Вы оформили вкид, Вам понравилось</b>']
            drug = random.choice(drugsss)
            await message.edit(drug)
            await asyncio.sleep(5)
            await message.edit("⭐ @ ")

        @app.on_message(filters.command("mum", prefixes=".") & filters.me)
        async def mum(client, message):
            mamka = [f'<b>❌ Мамаша не найдена</b>',f'<b> ✅ МАМАША НАЙДЕНА</b>' ]
            text = "<b>🔍 Поиск твоей мамки начался...</b>"
            await message.edit(str(text))
            await asyncio.sleep(3.0)
            text2 = "<b>🔍 Ищем твою мамашу на Авито... </b>"
            await message.edit(str(text2))
            await asyncio.sleep(1)
            text3 = random.choice(mamka)
            await message.edit(str(text3))
            await asyncio.sleep(3.0)
            text4 = "<b>🔍 Поиск твоей мамаши на свалке... </b>"
            await message.edit(str(text4))
            await asyncio.sleep(3.0)
            text5 = random.choice(mamka)
            await message.edit(str(text5))
            await asyncio.sleep(5.0)
            text6 = "⭐ @ "
            await message.edit(str(text6))

        @app.on_message(filters.command("gifspam", prefixes=".") & filters.me)
        def sendgif(app, message):
            qq = " ".join(str(message.command[2:]))
            for _ in range(int(message.command[1])):
                sleep(0.01)
                app.send_document(message.chat.id, qq)

        @app.on_message(filters.command("showdown", prefixes=".") & filters.me)
        def valentine(app, msg):
            msg.edit(f"<b>Начало через: 13s</b>")  # orange
            sleep(0.6)
            msg.edit(f"<b>Начало через: 12s</b>")  # red
            sleep(0.6)
            msg.edit(f"<b>Начало через: 11s</b>")  # orange
            sleep(0.6)
            msg.edit(f"<b>Начало через: 10s</b>")  # red
            sleep(0.6)
            msg.edit(f"<b>Начало через: 9s</b>")  # orange
            sleep(0.6)
            msg.edit(f"<b>Начало через: 8s</b>")  # red
            sleep(0.6)
            msg.edit(f"<b>Начало через: 7s</b>")  # orange
            sleep(0.6)
            msg.edit(f"<b>Начало через: 6s</b>")  # red
            sleep(0.6)
            msg.edit(f"<b>Начало через: 5s</b>")  # orange
            sleep(0.6)
            msg.edit(f"<b>Начало через: 4s</b>")  # red
            sleep(0.6)
            msg.edit(f"<b>Начало через: 3s</b>")  # orange
            sleep(0.6)
            msg.edit(f"<b>Начало через: 2s</b>")  # red
            sleep(0.6)
            msg.edit(f"<b>Начало через: 1s</b>")  # orange
            sleep(0.2)
            msg.edit(f"<b>Бу, блять! Ха-ха</b>") 
            sleep(1.2)
            msg.edit(f"<b>Просыпайтесь нахуй (Let's go!)</b>")  # orange
            sleep(1.3)
            app.send_message(msg.chat.id, f'''<b>Головы сияют на моей едкой катане</b>''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Голоса этих ублюдков по пятам бегут за нами</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Погружённый в Изанами, все колёса под глазами</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Похоронный марш гулей, на часах последний тик</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Моя тати — Бравл Шелли, я несу ей дробовик</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Ваши головы — мишени, я снесу их в один миг</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Никаких резких движений — ваш хилбар на один хит</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Динамайк трипл килл, ха, нервы на пределе</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Voice в моих ушах — я позабыл все дни недели</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Как на лезвии ножа и шквал патрон, летят шрапнели</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Psychokilla — весь мой шарм, вся эта мапа поредели</b>
            ''')
            sleep(1.5)
            app.send_message(msg.chat.id, f'''
            <b>Эй, погоди, мои парни на Стокгольме</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Мой showdown 1x1, и мои демоны все в форме</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Если я зайду к вам в лобби — оно станет вам могилой</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Если ты зайдешь — мне похуй, я не стартану и выйду, а-ха</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>По приказу Генерала Гавса!</b>
            ''')
            sleep(1.4)
            app.send_message(msg.chat.id, f'''
            <b>— Бро, тут вообще сложная ситуация, все границы позакрывали нахуй. Ваще пиздец полный. Ща просто едем ближе ко Львову, но во Львове тоже пиздец начался, поэтому хуй знает</b>
            ''')
            sleep(1.9)
            app.send_message(msg.chat.id, f'''
            <b>— Бля, чуваки, шутки шутками, но не занимайтесь хуйнёй, я вас умоляю. А-а-а!</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Эй, я как Вольт — называй неуловимый</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>De-Dead inside mode, я бегу по головам</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Оверсайз весь шмот, я на трапе тут и там</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Весь твой скилл — шаблон, я по рофлу на битах</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Зачем мне октагон? Могу выйти на финдах, ха</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Головы сияют на моей едкой катане</b>
          ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Голоса этих ублюдков по пятам бегут за нами</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Погружённый в Изанами, все колёса под глазами</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Генерал Гавс, ха, вижу вас без гема</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Я отдал приказ, и все умрут от реквиема</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Дота-рэп — топ чарт, ха, наебал систему</b>
            ''')
            sleep(1.3)
            app.send_message(msg.chat.id, f'''
            <b>Mute all chat, я на лям скупил все гемы, ха-ха</b>
            ''')
            sleep(1.4)
            app.send_message(msg.chat.id, f'''
            <b>Ха-а, бля</b>
            ''')

            sleep(0.5)
            
            
            app.send_message(message.chat.id, f'''
             <b> </b>
             ''')


        @app.on_message(filters.command("vopros", prefixes=".") & filters.me)
        def betaloves(_, msg):
            time = 0.4
            for i in range(1):
              sleep(0.001)
              msg.edit(f'''      
        🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        ''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦''')  # red
              sleep(0.001)
              msg.edit(f'''      
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦''')  # red
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        ''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        ''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        ''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        ''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦''')
              sleep(0.001)
              msg.edit(f'''   
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦⬛️⬛️⬛️🟦🟦
        🟦⬛️🟦🟦🟦⬛️🟦
        🟦🟦🟦🟦⬛️🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦⬛️🟦🟦🟦
        🟦🟦🟦🟦🟦🟦🟦
        ''')
            sleep(5)
            
            
            msg.edit(f'<b> </b>')

        @app.on_message(filters.command("id", prefixes=".") & filters.me)
        async def link(app, message):

            d = message.chat.id
            await app.send_message(message.chat.id,f''' <b>Айди этого чата\n</b><code>{d}</code>''')

        @app.on_message(filters.command("del", prefixes=".") & filters.me)
        async def link(app, message):
            try:
                timedel = int(message.text.split()[1])
                if timedel>400:
                    await message.edit("Нельзя ставить больше 400 секунд!")
            except IndexError:
                await message.edit("Вы не ввели число!\nПример:.del 60 текст")
            text = " ".join(message.command[2:])
            if not text:
                await message.edit("Вы не ввели сообщение!\nПример:.del 60 текст")
            await message.edit(text)
            await sleep(timedel)
            await message.delete()

        @app.on_message(filters.command("tag", prefixes=".") & filters.me)
        async def link(client, message):
            name = " ".join(message.command[1])
            text = " ".join(message.command[2:])
            if not text:
                text = "Лох"
            await message.delete()
            await client.send_message(message.chat.id, f'<a href="{name}">{text}</a>', disable_web_page_preview=True)

        @app.on_message(filters.command("tagall", prefixes=".") & filters.me)
        async def link(client, message):
            name = "tg://settings"
            text = " ".join(message.command[1:])
            if not text:
                text = "Лох"
            await message.delete()
            await client.send_message(message.chat.id, f'<a href={name}>{text}</a>', disable_web_page_preview=True)


        @app.on_message(filters.command("react", prefixes=".") & filters.me)
        async def link(app, message):
            try:
                g = int(message.text.split()[1])
            except IndexError:
                g = 5
                await message.edit("<b>Вы не ввели кол-во реакций!По умолчанию выбрано</b> <code> 5 </code> раз")
                await sleep(4)
            try:
                v = message.text.split()[2]
            except IndexError:
                v = "👍"
                await message.edit(f"<b>Вы не ввели смайл для спама!По умолчанию выбран</b>=>👍")
            h = await app.get_history(chat_id=message.chat.id, limit=g) # получаем историю сообщений (первые g)
            for x in h: # идем по списку
            #  y = x.from_user.id
                x = x.message_id # достаем ид сообщения
                #if y in call: можно добавить проверку на определенного человека/людей
                await app.send_reaction(message_id=x, chat_id=message.chat.id, emoji=v)
                await sleep(0.4)
            


        @app.on_message(filters.command("link", prefixes=".") & filters.me)
        async def link(client, message):
            link = message.command[1]
            text = " ".join(message.command[2:])
            await message.delete()
            await client.send_message(message.chat.id, f'<a href="{link}">{text}</a>', disable_web_page_preview=True)


        module_list['LinkInText'] = f'.link [link] [text]'
        file_list['LinkInText'] = 'link.py'

        @app.on_message(filters.command("time", prefixes=".") & filters.me)
        async def time(client, message):
            now = datetime.now()
            time_now = now.strftime("Date: %d/%m/%Y\nTime: %H:%M:%S")
            await message.edit(time_now)



        module_list['TimeNow'] = f'.time'
        file_list['TimeNow'] = 'time_now.py'




        @app.on_message(filters.command(["scr", "screenshot"], prefixes=".") & filters.private & filters.me)
        async def screenshot(client, message):
            quantity = int(message.command[1])
            await message.delete()
            for _ in range(quantity):
                await asyncio.sleep(0.1)
                await client.send(
                    functions.messages.sendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )


        module_list['Screenshot'] = f'.scr | .screenshot'
        file_list['Screenshot'] = 'screenshot.py'


        @app.on_message(filters.command("covid_ru", prefixes=".") & filters.me)
        async def covid_local(client, message):
            region = " ".join(message.command[1:])
            await message.edit("<code>Получение данных...</code>")
            covid = Covid(source="worldometers")
            try:
                local_status = covid.get_status_by_country_name(region)
                await message.edit(
                    "<b>=====🦠 Статистика COVID-19 🦠=====</b>\n"
                    + f"<b>Страна</b>: <code>{local_status['country']}</code>\n"
                    + "<b>==================================</b>\n"
                    + f"<b>🤧 Новые заражения</b>: <code>{local_status['new_cases']}</code>\n"
                    + f"<b>😷 Новые смерти</b>: <code>{local_status['new_deaths']}</code>\n"
                    + "<b>==================================</b>\n"
                    + f"<b>😷 Подтвержденные</b>: <code>{local_status['confirmed']}</code>\n"
                    + f"<b>❗️ Болеют:</b> <code>{local_status['active']}</code>\n"
                    + f"<b>⚠️ В тяжелом состоянии</b>: <code>{local_status['critical']}</code>\n"
                    + f"<b>💀 Всего смертей</b>: <code>{local_status['deaths']}</code>\n"
                    + f"<b>🚑 Всего выздоровели</b>: <code>{local_status['recovered']}</code>\n"
                )
            except ValueError:
                await message.edit(f'<code>Нет такой страны с названием  "{region}"</code>')


        module_list['StatisticsCovid19'] = f'.covid_[en|ru] [region]'
        file_list['StatisticsCovid19'] = 'covid.py'





        @app.on_message(filters.command("wiki", prefixes=".") & filters.me)
        async def wiki(client, message):
            lang = message.command[1]
            user_request = " ".join(message.command[2:])
            await message.edit("<b>Search info</b>")
            if user_request == "":
                wikipedia.set_lang("ru")
                user_request = " ".join(message.command[1:])
            try:
                if lang == "ru":
                    wikipedia.set_lang("ru")

                result = wikipedia.summary(user_request)
                await message.edit(
                    f"""<b>�����:</b>
        <code>{user_request}</code>
        
        <b>Info:</b>
        <code>{result}</code>"""
                )
            except Exception as exc:
                await message.edit(
                    f"""<b>Request:</b>
        <code>{user_request}</code>
        <b>Result:</b>
        <code>{exc}</code>"""
                )

        module_list['Wikipedia'] = f'.wiki [word]'
        file_list['Wikipedia'] = 'wiki.py'

        @app.on_message(filters.command("cum", prefixes=".") & filters.me)
        async def betaloves(_, message):
            for i in range(1):
                await message.edit(f'''
        Т҈̲͕͈̜̣̓̈́̕͜ы̸̡̮̦̜̣͕̖̤̮̎̌̐͞ О̷̧͓̣̤͌͆̃͊̿̚͠Б̵̡͓̫͍̯҇͗̅Р̸̪̝͙͓̙̗͓͊̃̉̈́̀͑͢͝Е̶̧͙̱̥̠̗̘̪̍͑͐̚͝Ч̵̨̫̟͔̜͙͔͉͇́̔͝Ё̶̢̩̣̒̏̋͝Н̵͙̳͇͎҇͑̾̽̀̾̈́̃͜?҉̡̩̞̤̰̭̳̖̅̂̽͒͑̈͊͡''')  
                await asyncio.sleep(2)
                await message.edit(f'''
        Г̱͕͍͔͖̘̗͎̠̦̝͓͓̫͍̳̜̠̜͐̅̋̓̋̀͐͐̐̾͒̒ͅл̲̲̟͈̣͇͓͙͇͈̞͕̱̘̬̞̳̖͈̫̲͖̅̏͋̀̆̍͌̐͂̃͆̔̆͊̄а͍̗̰̳̙̖̞̦͈͉̟̣͎̠̣̳̖͚͋͐͊͐̿́͛̐͆̌̌̈͛̔̉͊͛̃̉̀̐̊͗з̫͇̣͓̝̗̬̦̖͙͕͓̤̗͈̲͓̏̈́̍̋̀͊̑̒̒̋͋̊ͅа͍͖̞͓̙̲̬̜̰̣͓͍̮̝̮͚̟̞̐̄̉͐̾͆̇̔̌̓̂͒̚ͅ ''')  
                await asyncio.sleep(2)
                await message.edit(f'''
        П̯̰̜͙̱̭͈̙̯̖̏́̽̇͗͂̿̂͋̀̀̎͊о̣͇̲͚͚̬͔͚̗͍̦̏̋̓́͐̽̀̎̀̈л̞̝̮̣̪̞̳̲͍͚̮̜̝̦̯͐̑͒̏̇͌͋̒̔̅̆̍̓͗͊͆з̯̜̩̠̙̮̞͇̮̗̝̪̦̞̐͐̓͂̽͗̎̂͑͗̒̈̚ͅу̫̘̭͔̰̥̟͈̍͌͐̈̉͑̽̑̔̚ͅт̙͉̯͔̲̖̱̳̤͕̯̬̑́̎̓̉̿̎̑́ͅͅ''')  
                await asyncio.sleep(2)
                await message.edit(f'''
        у̫͓̠̩͍̰̰̥͈̱͚̞̥͊̐̎̔̊͊̅̎͗͛͋͊̚m͎̙̩̮̣̗̠͎̗͚̥̣̬̠͚̒́̂͑͌͌̆̀̐̈̓̀̈̀̑͛̊̈͒̐̆e̠̯͓̘͍̮̱͉̙̙̠̣̪̠̦̮͔̮̟̲̪̩̒̾̐̀̂̀̉̃̆́̾̏̑̀p͎͚͉͖̳̣̝̩̩̥̮͇͔̞̘̜̜̥̟̱̙͉͗̽͂̓͋͐͑̇͊́́͂͆͊̽͐́̓͆̐͊̊̚''')  
                await asyncio.sleep(2)

        @app.on_message(filters.command("purge", prefixes=".") & filters.me)
        async def purge(app, message):
            try:
                if message.reply_to_message:
                    r = message.reply_to_message.message_id
                    m = message.message_id
                    msgs = []
                    await message.delete()
                    while r != m:
                        msgs.append(int(r))
                        r += 1
                    await app.delete_messages(message.chat.id, msgs)
                    r = message.reply_to_message.message_id
                    msgs = []
                    while r != m:
                        msgs.append(int(r))
                        r += 1
                    await app.delete_messages(message.chat.id, msgs)
                    await app.send_message(message.chat.id, f"<b>Messages deleted!</b>")
                else:
                    await message.edit("<i>I don't see reply</i>")
            except:
                await message.edit("<i>Don't have permision.</i>")

        @app.on_message(filters.command( "music", prefixes=".") & filters.me)
        async def send_music(app, message):
            await message.edit("Search...")
            song_name = ""
            if len(message.command) > 1:
                song_name = " ".join(message.command[1:])
            elif message.reply_to_message and len(message.command) == 1:
                song_name = (
                        message.reply_to_message.text or message.reply_to_message.caption
                )
            elif not message.reply_to_message and len(message.command) == 1:
                await message.edit("Enter the name of the music")
                await asyncio.sleep(2)
                await message.delete()
                return

            song_results = await app.get_inline_bot_results(bots, song_name)

            try:
                # send to Saved Messages because hide_via doesn't work sometimes
                saved = await app.send_inline_bot_result(
                    chat_id="me",
                    query_id=song_results.query_id,
                    result_id=song_results.results[0].id
                )

                # forward as a new message from Saved Messages
                saved = await app.get_messages("me", int(saved.updates[1].message.id))
                reply_to = (
                    message.reply_to_message.message_id
                    if message.reply_to_message
                    else None
                )
                await app.send_audio(
                    chat_id=message.chat.id,
                    audio=str(saved.audio.file_id),
                    reply_to_message_id=reply_to,
                )

                # delete the message from Saved Messages
                await app.delete_messages("me", saved.message_id)
            except TimeoutError:
                await message.edit("That didn't work out")
                await asyncio.sleep(2)
            await message.delete()


        # from athphane app
        @app.on_message(filters.command( "lyrics", prefixes=".") & filters.me)
        async def send_music(app, message):
            try:
                cmd = message.command
                song_name = ""
                if len(cmd) > 1:
                    song_name = " ".join(cmd[1:])
                elif message.reply_to_message:
                    if message.reply_to_message.audio:
                        song_name = f"{message.reply_to_message.audio.title} {message.reply_to_message.audio.performer}"
                    elif len(cmd) == 1:
                        song_name = message.reply_to_message.text
                elif not message.reply_to_message and len(cmd) == 1:
                    await message.edit("Give a song name")
                    await asyncio.sleep(2)
                    await message.delete()
                    return

                await message.edit(f"Getting lyrics for `{song_name}`")
                lyrics_results = await app.get_inline_bot_results("ilyricsbot", song_name)

                try:
                    # send to Saved Messages because hide_via doesn't work sometimes
                    saved = await app.send_inline_bot_result(
                        chat_id="me",
                        query_id=lyrics_results.query_id,
                        result_id=lyrics_results.results[0].id,
                        hide_via=True,
                    )
                    await asyncio.sleep(3)

                    # forward from Saved Messages
                    await app.copy_message(
                        chat_id=message.chat.id,
                        from_chat_id="me",
                        message_id=saved.updates[1].message.id,
                    )

                    # delete the message from Saved Messages
                    await app.delete_messages("me", saved.updates[1].message.id)
                except TimeoutError:
                    await message.edit("That didn't work out")
                    await asyncio.sleep(2)
                await message.delete()
            except Exception as e:
                print(e)
                await message.edit("`Failed to find lyrics`")
                await asyncio.sleep(2)
                await message.delete()




        @app.on_message(filters.command("ping", prefixes=".") & filters.me)
        async def ping(client, message):
            start1 = perf_counter()
            await message.edit("test Ping..")
            end1 = perf_counter()

            start2 = perf_counter()
            await message.edit("test pIng..")
            end2 = perf_counter()

            start3 = perf_counter()
            await message.edit("test piNg...")
            end3 = perf_counter()

            start4 = perf_counter()
            await message.edit("test pinG...")
            end4 = perf_counter()

            pinges = ((end1 + end2 + end3 + end4) / 4) - ((start1 + start2 + start3 + start4) / 4)
            ping = pinges * 1000

            if 0 <= ping <= 199:
                connect = "🟢 Stable"
            if 199 <= ping <= 400:
                connect = "🟠 Good"
            if 400 <= ping <= 600:
                connect = "🔴 Not stable"
            if 600 <= ping:
                connect = "⚠ Check you network connection"
            await message.edit(f"<b>🏓 Pong\n📶</b> {round(ping)} ms\n{connect}")


        @app.on_message(filters.command( ["quote","q"], prefixes=".") & filters.me)
        async def quote_cmd(app, message):
            if not message.reply_to_message:
                return await message.edit("<b>Выберите сообщение для цитаты!</b>")

            if len(message.command) > 1 and message.command[1].isdigit():
                count = int(message.command[1])
                if count < 1:
                    count = 1
                elif count > 15:
                    count = 15
            else:
                count = 1

            is_png = "!png" in message.command or "!file" in message.command
            send_for_me = "!me" in message.command or "!ls" in message.command
            no_reply = "!noreply" in message.command or "!nr" in message.command

            messages = list(
                filter(
                    lambda x: x.message_id < message.message_id,
                    await app.get_messages(
                        message.chat.id,
                        range(
                            message.reply_to_message.message_id,
                            message.reply_to_message.message_id + count,
                        ),
                    ),
                )
            )

            if no_reply:
                messages[0].reply_to_message = None

            if send_for_me:
                await message.delete()
                message = await app.send_message("me", "<b>Generating...</b>")
            else:
                await message.edit("<b>Generating...</b>")

            url = "https://quotes.fl1yd.su/generate"
            params = {
                "messages": [
                    await render_message(app, msg) for msg in messages if not msg.empty
                ],
                "quote_color": "#162330",
                "text_color": "#fff",
            }

            response = requests.post(url, json=params)
            if not response.ok:
                return await message.edit(
                    f"<b>Quotes API error!</b>\n" f"<code>{response.text}</code>"
                )

            file_io = BytesIO(response.content)
            file_io.name = "sticker.png" if is_png else "sticker.webp"
            await message.edit("<b>sending...</b>")

            try:
                func = app.send_document if is_png else app.send_sticker
                chat_id = "me" if send_for_me else message.chat.id
                await func(chat_id, file_io)
            except errors.RPCError as e:  # no rights to send stickers, etc
                await message.edit(f"<b>Telegram API error!</b>\n" f"<code>{e}</code>")
            else:
                await message.delete()


        @app.on_message(filters.command( ["fakequote", "fq"], prefixes=".") & filters.me)
        async def fake_quote_cmd(app: app, message: types.Message):
            if not message.reply_to_message:
                return await message.edit("<b>Specify message for fake quote</b>")

            is_png = "!png" in message.command or "!file" in message.command
            send_for_me = "!me" in message.command or "!ls" in message.command
            no_reply = "!noreply" in message.command or "!nr" in message.command

            fake_quote_text = " ".join(
                [
                    arg
                    for arg in message.command[1:]
                    if arg not in ["!png", "!file", "!me", "!ls", "!noreply", "!nr"]
                ]  # remove some special arg words
            )

            if not fake_quote_text:
                return await message.edit("<b>Fake quote text is empty</b>")

            q_message = await app.get_messages(
                message.chat.id, message.reply_to_message.message_id
            )
            q_message.text = fake_quote_text
            q_message.entities = None
            if no_reply:
                q_message.reply_to_message = None

            if send_for_me:
                await message.delete()
                message = await app.send_message("me", "<b>Generating...</b>")
            else:
                await message.edit("<b>Generating...</b>")

            url = "https://quotes.fl1yd.su/generate"
            params = {
                "messages": [await render_message(app, q_message)],
                "quote_color": "#162330",
                "text_color": "#fff",
            }

            response = requests.post(url, json=params)
            if not response.ok:
                return await message.edit(
                    f"<b>Quotes API error!</b>\n" f"<code>{response.text}</code>"
                )

            file_io = BytesIO(response.content)
            file_io.name = "sticker.png" if is_png else "sticker.webp"
            await message.edit("<b>sending...</b>")

            try:
                func = app.send_document if is_png else app.send_sticker
                chat_id = "me" if send_for_me else message.chat.id
                await func(chat_id, file_io)
            except errors.RPCError as e:  # no rights to send stickers, etc
                await message.edit(f"<b>Telegram API error!</b>\n" f"<code>{e}</code>")
            else:
                await message.delete()


        files_cache = {}


        async def render_message(app: app, message: types.Message) -> dict:
            async def get_file(file_id) -> str:
                if file_id in files_cache:
                    return files_cache[file_id]

                file_name = await app.download_media(file_id)
                with open(file_name, "rb") as f:
                    content = f.read()
                os.remove(file_name)
                data = base64.b64encode(content).decode()
                files_cache[file_id] = data
                return data

            # text
            if message.photo:
                text = message.caption if message.caption else ""
            elif message.poll:
                text = get_poll_text(message.poll)
            elif message.sticker:
                text = ""
            else:
                text = get_reply_text(message)

            # media
            if message.photo:
                media = await get_file(message.photo.file_id)
            elif message.sticker:
                media = await get_file(message.sticker.file_id)
            else:
                media = ""

            # entities
            entities = []
            if message.entities:
                for entity in message.entities:
                    entities.append(
                        {
                            "offset": entity.offset,
                            "length": entity.length,
                            "type": entity.type,
                        }
                    )

            def move_forwards(msg: types.Message):
                if msg.forward_from:
                    msg.from_user = msg.forward_from
                elif msg.forward_sender_name:
                    msg.from_user.id = 0
                    msg.from_user.first_name = msg.forward_sender_name
                    msg.from_user.last_name = ""
                elif msg.forward_from_chat:
                    msg.sender_chat = msg.forward_from_chat

            move_forwards(message)

            # author
            author = {}
            if message.from_user:
                author["id"] = message.from_user.id
                author["name"] = get_full_name(message.from_user)
                if message.chat.type != "supergroup" or message.from_user.id == 0:
                    author["rank"] = ""
                else:
                    try:
                        member = await message.chat.get_member(message.from_user.id)
                    except errors.UserNotParticipant:
                        author["rank"] = ""
                    else:
                        author["rank"] = getattr(member, "title", "") or (
                            "owner"
                            if member.status == "creator"
                            else "admin"
                            if member.status == "administrator"
                            else ""
                        )

                if message.from_user.id == 0 or not message.from_user.photo:
                    author["avatar"] = ""
                else:
                    author["avatar"] = await get_file(message.from_user.photo.big_file_id)
            else:
                author["id"] = message.sender_chat.id
                author["name"] = message.sender_chat.title
                author["rank"] = "channel" if message.sender_chat.type == "channel" else ""

                if message.sender_chat.photo:
                    author["avatar"] = await get_file(message.sender_chat.photo.big_file_id)
                else:
                    author["avatar"] = ""
            author["via_bot"] = message.via_bot.username if message.via_bot else ""

            # reply
            reply = {}
            reply_msg = message.reply_to_message
            if reply_msg and not reply_msg.empty:
                move_forwards(reply_msg)

                if reply_msg.from_user:
                    reply["id"] = reply_msg.from_user.id
                    reply["name"] = get_full_name(reply_msg.from_user)
                else:
                    reply["id"] = reply_msg.sender_chat.id
                    reply["name"] = reply_msg.sender_chat.title

                reply["text"] = get_reply_text(reply_msg)

            return {
                "text": text,
                "media": media,
                "entities": entities,
                "author": author,
                "reply": reply,
            }


        def get_audio_text(audio: types.Audio) -> str:
            if audio.title and audio.performer:
                return f" ({audio.title} — {audio.performer})"
            elif audio.title:
                return f" ({audio.title})"
            elif audio.performer:
                return f" ({audio.performer})"
            else:
                return ""


        def get_reply_text(reply: types.Message) -> str:
            return (
                "📷 Photo" + ("\n" + reply.caption if reply.caption else "")
                if reply.photo
                else get_reply_poll_text(reply.poll)
                if reply.poll
                else "📍 Location"
                if reply.location or reply.venue
                else "👤 Contact"
                if reply.contact
                else "🖼 GIF"
                if reply.animation
                else "🎧 Music" + get_audio_text(reply.audio)
                if reply.audio
                else "📹 Video"
                if reply.video
                else "📹 Videomessage"
                if reply.video_note
                else "🎵 Voice"
                if reply.voice
                else (reply.sticker.emoji + " " if reply.sticker.emoji else "") + "Sticker"
                if reply.sticker
                else "💾 File " + reply.document.file_name
                if reply.document
                else "🎮 Game"
                if reply.game
                else "🎮 set new record"
                if reply.game_high_score
                else f"{reply.dice.emoji} - {reply.dice.value}"
                if reply.dice
                else (
                    "👤 joined the group"
                    if reply.new_chat_members[0].id == reply.from_user.id
                    else "👤 invited %s to the group"
                         % (get_full_name(reply.new_chat_members[0]))
                )
                if reply.new_chat_members
                else (
                    "👤 left the group"
                    if reply.left_chat_member.id == reply.from_user.id
                    else "👤 removed %s" % (get_full_name(reply.left_chat_member))
                )
                if reply.left_chat_member
                else f"✏ changed group name to {reply.new_chat_title}"
                if reply.new_chat_title
                else "🖼 changed group photo"
                if reply.new_chat_photo
                else "🖼 removed group photo"
                if reply.delete_chat_photo
                else "📍 pinned message"
                if reply.pinned_message
                else "🎤 started a new video chat"
                if reply.voice_chat_started
                else "🎤 ended the video chat"
                if reply.voice_chat_ended
                else "🎤 invited participants to the video chat"
                if reply.voice_chat_members_invited
                else "👥 created the group"
                if reply.group_chat_created or reply.supergroup_chat_created
                else "👥 created the channel"
                if reply.channel_chat_created
                else reply.text or "unsupported message"
            )


        def get_poll_text(poll: types.Poll) -> str:
            text = get_reply_poll_text(poll) + "\n"

            text += poll.question + "\n"
            for option in poll.options:
                text += f"- {option.text}"
                if option.voter_count > 0:
                    text += f" ({option.voter_count} voted)"
                text += "\n"

            text += f"Total: {poll.total_voter_count} voted"

            return text


        def get_reply_poll_text(poll: types.Poll) -> str:
            if poll.is_anonymous:
                text = "📊 Anonymous poll" if poll.type == "regular" else "📊 Anonymous quiz"
            else:
                text = "📊 Poll" if poll.type == "regular" else "📊 Quiz"
            if poll.is_closed:
                text += " (closed)"

            return text


        def get_full_name(user: types.User) -> str:
            name = user.first_name
            if user.last_name:
                name += " " + user.last_name
            return name


        @app.on_message(filters.command('qh', prefixes=".") & filters.me)
        async def squotes_help(app, message):
            await message.edit("""**!q [reply] [count] [args] - Создать цитату 
        Доступные аргументы: !png — отправить цитату в формате png; !me — отправить цитату в сохраненные сообщения; !noreply - сделать цитату без ответа сообщение.
        
        !fq [ответ] [аргументы] [текст] - Создать фальшивую цитату**""")
        module_list['Squotes'] = f"Many commands. View them: .squotes_help."
        file_list['Squotes'] = 'squotes.py'


        @app.on_message(filters.command("sendchel", prefixes=".") & filters.me)
        def sendgif(app, message):
            for _ in range(int(message.command[1])):
                sleep(0.01)
                app.send_document(message.chat.id, "https://c.tenor.com/8EFfe9cshekAAAAS/%D1%87%D0%B5%D0%BB-%D1%85%D0%B0%D1%80%D0%BE%D1%88.gif")

        @app.on_message(filters.command("sendrock", prefixes=".") & filters.me)
        def sendgif(app, message):
            for _ in range(int(message.command[1])):
                sleep(0.01)
                app.send_document(message.chat.id, "https://tenor.com/bMX5E.gif")



        @app.on_message(filters.command("dead", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = textded.split("\n")
            e = True
            etime = int(msg.text.split('.dead ', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 8:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'❤️{i} ❤️')
                        sleep(time/6)
                        msg.edit(f'🧡 {i} 🧡')
                        sleep(time/6)
                        msg.edit(f'💛 {i} 💛')
                        sleep(time/6)
                        msg.edit(f'💚 {i} 💚')
                        sleep(time/6)
                        msg.edit(f'💙 {i} 💙')
                        sleep(time/6)
                        msg.edit(f'💜 {i} 💜')
                        sleep(time/6)
                        msg.edit(f'🖤 {i} 🖤')
                        sleep(time/6)
                        msg.edit(f'🤍 {i} 🤍')
                        sleep(time/6)
                    except:
                        pass
            
            
            msg.edit(f'<b> Script</b>')
            msg.edit(f'<b>⭐ Script(</b>')

        textded = '''
        <b> Я дед инсайд </b>
        <b> Мне 9 лет </b>
        <b> И я хочу в Психокидс </b>
        '''

        @app.on_message(filters.command("clock", prefixes=".") & filters.me)
        async def clockscmd(self, message):
            for _ in range(12):
                for clock in ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]:
                    await message.edit(clock)
                    await sleep(0.3)



        @app.on_message(filters.command("type", prefixes=".") & filters.me)
        def valentine(_, msg):
            orig_text = msg.text.split(".type ", maxsplit=1)[1]
            text = orig_text
            tbp = ""
            typing_symbol = "█"
            while (tbp != orig_text):
                try:
                    msg.edit(tbp + typing_symbol)
                    sleep(0.05)

                    tbp = tbp + text[0]
                    text = text[1:]

                    msg.edit(tbp)
                    sleep(0.05)

                except FloodWait as e:
                    sleep(e.x)






        textded1 = '''
        <b>спокойной ночи зайка 💚</b>
        <b>спокойной ночи солнышко 💛</b>
        <b>спокойной ночи котёнок ❤</b>️
        <b>спокойной ночи цветочек 💙</b>
        <b>спокойной ночи ангелочек 💜</b>
        <b>спокойной ночи принцесса 💓</b>
        <b>спокойной ночи красотка 💕</b>
        <b>спокойной ночи милашка 💖</b>
        <b>спокойной ночи симпатяжка 💗</b>
        <b>спокойной ночи бусинка 💘</b>
        <b>❤я❤</b>️
        <b>💚 тебя 💚</b>
        <b>💙 очень 💙</b>
        <b>💛 сильно 💛</b>
        <b>💜 люблю 💜</b>
        '''


        @app.on_message(filters.command("compli", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = comp.split("\n")
            e = True
            etime = int(msg.text.split('.compli ', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                    except:
                        pass
           
             
            


        @app.on_message(filters.command("night", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = textded1.split("\n")
            e = True
            etime = int(msg.text.split('.night ', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                    except:
                        pass
            
            

        @app.on_message(filters.command("random", prefixes=".") & filters.me)
        def random_(_, msg):
            random_number = str(random.randint(0, int(msg.command[1])))
            msg.edit(roi + random_number)



        too = random.randint(0, 100)
        roi = f'<b> Случайное число: </b>'

        @app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
        def valentine(app, message):
            
            
            app.send_message(message.chat.id,f'<b>Ты гуль?</b>')
            sleep(2)

            app.send_message(message.chat.id,f'<i>Я тоже</i>')
            sleep(0.09)
            app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEEDZiI8ZlrkTWVAVlsaJ1yfd63euS2AACMgwAAgqBoEs52ePcv8NaIiME")
            sleep(5)
            i = 1000
            while i > 0:
                try:
                    app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
                except FloodWait as e:
                    sleep(e.x)

                i -= 7
                sleep(0)

            if(end_message != ''):
                app.send_message(message.chat.id, end_message)

        @app.on_message(filters.command("spam", prefixes=".") & filters.me)
        async def spam(app, message):
            await app.join_chat("starzedscripts")
            spams = " ".join(message.command[2:])
            if not spams:
                await message.edit("<b>Вы не ввели слово для спама!\nПример:</b><code>.spam 10 текст</code>")   
                spams = "@starzedscripts"
                await sleep(3)
            try:
                x = int(message.command[1])
            except IndexError:
                await message.edit("<b>Вы не ввели число для спама!\nПример:</b><code>.spam 10 текст</code>")
                x = 5  
            for _ in range(x):
                await sleep(0.01)
                await app.send_message(message.chat.id, spams)
           




        @app.on_message(filters.command("oxy", prefixes=".") & filters.me)
        def hent(Client,message):
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMBxiM2YMPTajpQABvwszy0vZDRm-8BAAAi4QAAJa0IFICLzmU39m9sYjBA")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMCBiM2ZYX5ishECYmcff0M_nUwdKegACqhAAAol8gEh_KDETWzwMoSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMCJiM2Zcsc0h07Ft3URDUumA9jiATgACZhMAAkSZgEic77gNT5yfcyME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMCViM2ZgyrgjetzfbUzrxU41dD70bwACwhMAAhFPgUitYgUXV6XhNSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMChiM2ZjT3SHa1fAAjVxKFRPtlxnuwAC-Q8AAkizgUg1oPltMoqHDCME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMCpiM2ZoFjE3V5AYQ4M5QZleuP7iDwACvREAAj6deUhXRIpi8ND4lSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMCxiM2Zqkri9vLy-Mfih23ZRVk0KcAACthUAAlnPgUgr9A1ygKcCRyME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMC5iM2ZtmQlHoCVqnPYpfrTwT2pq-QAC0xAAAnxFgUiGdee3rCqq8SME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDBiM2ZwOhiXhhh2IK8wqbqrwmJmTAACyRAAAj9igUhZh24PjIvL3SME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDJiM2Z27QZo0bEdZ5EQOuaJY1cTCwACVxEAAgg9gEhH7Fkjt--PiSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDRiM2Z5bCqndSxztYdcux1cXjqLqAACWBEAAq3FeUgci-WzxbxyKSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDZiM2Z8ffFWKVjUeTQZI19nq3vODQAC7BEAAgrKeUirYZDwzJ0lPSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDhiM2Z_EYVcuV6O_413q5VXhqyJDAACnRAAAqfteUjaUWYZjYhLHyME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDpiM2aCpa3H-D0DcXl3yaFsL7QqNQADEgAC5GaASGHKEVWl9aL-IwQ")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMDxiM2aGBd5ZV4VuXXbec0Zobm2PIAACvBEAAk9kgEincSdKyTbwiiME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMD5iM2aLcxua6gsmG-wWhhG9iD8L2AACCA8AAh7deUjP85EpAAEqSLgjBA")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMEFiM2aP1eQ4gBMRjFne4mrymYyFTQACwxAAAiT-gUg4rv5-pK24DiME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMERiM2aSCrxX5LfJ9PTvLwzASEjEnAACehMAApkzeEiF9LtCQAXLBSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMEZiM2aVccKJXH9WYPj4VzqD0YjKHQACmhAAAg2zgEimqztzXZrPaCME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMEhiM2aYg_T-8QNqKqFN424eByCbAwACVBIAAnvmgUi0ZiwT3vKe-CME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMEpiM2aadWyBUaaR521iggvpSiJlWgACzhUAAo0NgUiRVq5vwqu_ciME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMExiM2aelE62VNjdNPrmyMBSi8uIGwACwhAAAsS0eUi7TAh9IQEofyME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEME5iM2ahSC5wdQY7aes0qx0NcM4r-wACoA8AAqa1eEiMC9j3RVeMQiME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFBiM2aj9MRFsW3lp-JFBdrlwslVKwAClREAAlFgeEiCBWpR-era_iME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFJiM2amr6CC-MaA_qS3_Ep5pBjpZAACihYAAsSUgUizj25gJ7ZOhSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFRiM2aoh7eX6VJcw5ETODR2GgdV7gACKBAAAobFgUjkFnLCWmwPRSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFZiM2arX4GbYA0FzWILZq9YgCGfSgACKRAAAjTkgEgtLWdO0MDWWyME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFhiM2atwBkrG_0gDSK2s_r8epJXHgAC1xUAAhKygUgX4xBUCIlQ9yME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFpiM2awymiDTVEuTRH2w_b8W4QIDAACJxEAAt4reEiDr-qYCekYKyME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMFxiM2a85AfcyEl-3KdX7Rg_9kp4WAACkxEAAi7GgUjJo6jLrKEe9iME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMF5iM2a-F1Ykl4Loax3P4XMwtLVY4gACTg8AAjtZgEiGGyY2T1s96yME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMGBiM2bBPsqIf0kx8mvAZbKIoF7tLgAC0REAAoLygUh9Dbyifhfe0SME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMGJiM2bD5Fbp05K7rV0d_X1-4FmrJgACqBEAAgqMgEjomgZtph1z3SME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMGRiM2bQY_PoAvNYEh9i1EmRgaqxAANrFAAEgUgBznuw9IIL4SME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMGhiM2b-JGAh6SWLHMfWrfUU_LrGmAACAhIAAr5ogUjgw0vxucSwISME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMGpiM2cBHr8qCEyntyvBRAzuCd_UBwACzhIAAhphgEiiE2_W3aBlgSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMGxiM2cEfYi_rymxdBLYysX0EatTSAACfxUAAiOIgUi2qXTmARTYMSME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMHBiM2cGW4OCvQKCJ1E9zFq5se0oEAACahUAAh-ngUgWYUx1XJjK2CME")
          sleep(16.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMHJiM2cJsK26klxsAbjpLzcAAdPSEqAAAt4TAALCPYBIq2P7QoIPNDcjBA")
          sleep(15.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMHRiM2cLCZ6WiSbL2yAAAdWGtmL5wGkAAoIRAALhqoBIWkI4RFFx5PkjBA")
          sleep(15.0)
          app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEMHZiM2cNkVhHILmo5HctN4Uqyy07WQAChxIAAuYWgEjOLbzKOt36-yME")
          sleep(15.0)
          
        

        @app.on_message(filters.command("spamst", prefixes=".") & filters.me)
        def spamst(app, message):
            
            
            for _ in range(int(message.command[1])):
                sleep(0.01)
                app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEEDZiI8ZlrkTWVAVlsaJ1yfd63euS2AACMgwAAgqBoEs52ePcv8NaIiME")


    




       
        @app.on_message(filters.command("help", prefixes="/") & filters.me)
        def valentine(app, message):
            app.send_message(message.chat.id,f'''
        📙<b> Команды:</b> \n
        <b>https://telegra.ph/Komandy-Nex1n-skripta-04-28</b> ''', disable_web_page_preview = True)





        @app.on_message(filters.command("profile", prefixes="/") & filters.me)
        def help(app, message): 
            if message.from_user.id in {my_id, j_id, a_id, v_id, n_id}:
                app.send_message(message.chat.id, f'''
💾<b> Профиль:
</b> <b> Пользователь:</b><code> {message.from_user.first_name}</code>
<i><b> PREMIUM </b>- {random.choice(a)}</i>
<b> Chat_ID: </b><code> {message.chat.id}</code>
<b> User_ID: </b><code> {message.from_user.id}</code>''')
            else:
                app.send_message(message.chat.id,f'''
💾<b> Профиль:</b>
<b> Пользователь:
</b><code> {message.from_user.first_name}</code>
<i><b> PREMIUM </b>- LOX</i>
<b> Chat_ID: </b><code> {message.chat.id}</code>
<b> User_ID: </b><code> {message.from_user.id}</code>''',
                    disable_web_page_preview=True)
            

        @app.on_message(filters.command("maslo", prefixes=".") & filters.me)
        def betalove(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f"<b>я</b>")  # red
                sleep(time)
                msg.edit(f"<b>я люблю</b>")  # orange
                sleep(time)
                msg.edit(f"<b>я люблю когда</b>")  # orange
                sleep(time)
                msg.edit(f"<b>я люблю когда волосатые</b>")  # red
                sleep(time)
                msg.edit(f"<b>я люблю когда волосатые мужики</b>")  # orange
                sleep(time)
                msg.edit(f"<b>я люблю когда волосатые мужики обмазываются</b>")  # red
                sleep(time)
                msg.edit(f"<b>я люблю когда волосатые мужики обмазываются маслом 🧈</b>")  # orange
                sleep(5)
                
                
                
                

        @app.on_message(filters.command("football", prefixes=".") & filters.me)
        def betalove(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f"<b>⚽️ Вы зашли на футбольное поле, вам предстоит забить пенальти, чтобы победить</b>")  # red
                sleep(2)
                msg.edit(f"<b>⏳ Подготовка к игре.</b>")  # orange
                sleep(2)
                msg.edit(f"<b>⌛ Подготовка к игре..</b>")  # orange
                sleep(time)
                msg.edit(f"<b>⏳ Подготовка к игре...</b>")  # red
                sleep(time)
                msg.edit(f"<b>⚽ Удар.</b>")  # orange
                sleep(time)
                msg.edit(f"<b>⚽ Удар..</b>")  # red
                sleep(time)
                msg.edit(f"<b>⚽ Удар...</b>")  # orange
                sleep(time)
                msg.edit(random.choice(foot))
                sleep(5)
                
                
                
                msg.edit(f'<b>⭐Script  </b>')

        foot = ["<b>❌ К сожалению, вы проиграли..</b>", "<b>✅ Вы забили гол и победили в игре!</b>"]



     


        @app.on_message(filters.command("kill", prefixes=".") & filters.me)
        def betalove(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
                sleep(3)
                msg.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
                sleep(2)
                msg.edit(f"<b>⏳ [ 5s ]</b>")  # orange
                sleep(time)
                msg.edit(f"<b>⌛ [ 4s ]</b>")  # red
                sleep(time)
                msg.edit(f"<b>⏳ [ 3s ]</b>")  # orange
                sleep(time)
                msg.edit(f"<b>⌛ [ 2s ]</b>")  # red
                sleep(time)
                msg.edit(f"<b>⏳ [ 1s ]</b>")  # orange
                sleep(time)
                msg.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
                sleep(time)
                msg.edit(f"<b>👀 Поиск.</b>")  # orange
                sleep(time)
                msg.edit(f"<b>👀 Поиск..</b>")  # orange
                sleep(time)
                msg.edit(f"<b>👀 Поиск...</b>")  # orange
                sleep(time)
                msg.edit(f"<b>👀 Поиск.</b>")  # orange
                sleep(time)
                msg.edit(f"<b>👀 Поиск..</b>")
                sleep(time)
                msg.edit(f"<b>👀 Поиск...</b>")
                sleep(time)
                msg.edit(random.choice(kill))
                sleep(5)
                
                
                msg.edit(f'<b> @ </b>')
                msg.edit(f'<b>⭐ @ </b>')

        kill = ["<b>🔪 Убийца нашел тебя, к сожалению ты спрятался плохо и был убит</b>", "<b>⚔️Убийца не нашел тебя, вы  очень хорошо спрятались.</b>"]



        @app.on_message(filters.command("jopa", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = jopa.split("\n")
            e = True
            etime = int(msg.text.split('.jopa ', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                    except:
                        pass
            
            
            msg.edit(f'<b> @ </b>')
            msg.edit(f'<b>⭐ @ </b>')

        @app.on_message(filters.command("love", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = love.split("\n")
            e = True
            etime = int(msg.text.split('.love', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                    except:
                        pass
            
            
            msg.edit(f'<b> @ </b>')
            msg.edit(f'<b>⭐ @ </b>')

        @app.on_message(filters.command("zxc", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = zxc.split("\n")
            e = True
            etime = int(msg.text.split('.zxc', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                    except:
                        pass
            
            
            msg.edit(f'<b> @ </b>')
            msg.edit(f'<b>⭐ @</b>')


        @app.on_message(filters.command("moons", prefixes=".") & filters.me)
        async def moons(self, message):
            for _ in range(10):
                for moon in ['🌝', '🌚']:
                    await message.edit(moon)
                    await sleep(0.3)

        @app.on_message(filters.command("moons2", prefixes=".") & filters.me)
        async def moons2(self, message):
            for _ in range(10):
                for moon2 in ['🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔']:
                    await message.edit(moon2)
                    await sleep(0.3)

        @app.on_message(filters.command("dick", prefixes=".") & filters.me)
        async def dick(self, message):
            await message.edit('\u2060      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
            await sleep(1)
            await message.edit('\u2060    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
            await sleep(1)
            await message.edit('\u2060  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     '
                '🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
            await sleep(1)
            await message.edit('\u2060💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    '
                '🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
            await sleep(1)
            await message.edit('\u2060💦💦\n💦\n💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    '
                '🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')

        @app.on_message(filters.command("ziga", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = ziga.split("\n\n")
            e = True
            etime = int(msg.text.split('.ziga', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                        msg.edit(f'{i}')
                        sleep(time)
                    except:
                        pass
            
            
            msg.edit(f'<b> @ </b>')
            msg.edit(f'<b>⭐ @ </b>')










        @app.on_message(filters.command("like", prefixes=".") & filters.me)
        def betaloves(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f'''      
        🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦🟦🟦🟦🟦🟦''')
                sleep(0.001)
                msg.edit(f'''
        🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦⬜️🟦🟦🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦⬜️⬜️⬜️🟦⬜️🟦
        🟦🟦🟦🟦🟦🟦🟦🟦''')
                sleep(5)
                
                
                msg.edit(f'<b>⭐ @ </b>')

        @app.on_message(filters.command("spamstlike", prefixes=".") & filters.me)
        def spam(app, message):
            
            
            for _ in range(int(message.command[1])):
                sleep(0.01)
                app.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEFv5iJ5pNJ8hHeR_OizC4Y1JudX88CwAC-wkAAjVTmEs0H1r2bfL2GSME")


       




        @app.on_message(filters.command("dislike", prefixes=".") & filters.me)
        def betaloves(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f'''
        🟥''')  # red
                sleep(0.001)
                msg.edit(f'''
        🟥🟥''')  # red
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥🟥🟥🟥🟥''')
                sleep(0.001)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥🟥🟥🟥🟥🟥''')
                sleep(1)
                msg.edit(f'''
        🈲🈲🈲🈲🈲🈲🈲🈲
        🈲🈲⬜️⬜️⬜️🈲⬜️🈲
        🈲🈲⬜️⬜️⬜️🈲⬜️🈲
        🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
        🈲🈲🈲🈲⬜️🈲🈲🈲
        🈲🈲🈲🈲🈲🈲🈲🈲''')
                sleep(1)
                msg.edit(f'''
        🟥🟥🟥🟥🟥🟥🟥🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥⬜️⬜️⬜️🟥⬜️🟥
        🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
        🟥🟥🟥🟥⬜️🟥🟥🟥
        🟥🟥🟥🟥🟥🟥🟥🟥
        ''')
                sleep(1)
                msg.edit(f'''
        🈲🈲🈲🈲🈲🈲🈲🈲
        🈲🈲⬜️⬜️⬜️🈲⬜️🈲
        🈲🈲⬜️⬜️⬜️🈲⬜️🈲
        🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
        🈲🈲🈲🈲⬜️🈲🈲🈲
        🈲🈲🈲🈲🈲🈲🈲🈲''')
                sleep(4)
                
                
                msg.edit(f'<b>⭐ @ </b>')

        @app.on_message(filters.command("loves", prefixes=".") & filters.me)
        def betaloves(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f'''
        ✨✨✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨❤️✨✨❤️✨
        ✨❤️❤️❤️❤️✨
        ✨✨✨❤️❤️✨
        ✨✨❤️✨❤️✨
        ✨❤️✨✨❤️✨
        ✨✨✨✨✨✨''')  # red
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨✨❤️❤️✨✨
        ✨✨❤️❤️✨✨
        ✨✨❤️❤️✨✨
        ✨✨❤️❤️✨✨
        ✨✨✨✨✨✨''')  # red
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨❤️✨✨✨✨
        ✨❤️❤️❤️✨✨
        ✨❤️✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨❤️✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨❤️✨✨❤️✨
        ✨❤️✨✨❤️✨
        ✨❤️❤️❤️❤️✨
        ✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨
        ✨❤️❤️❤️❤️✨
        ✨❤️✨✨❤️✨
        ✨❤️❤️❤️❤️✨
        ✨✨✨❤️❤️✨
        ✨✨❤️✨❤️✨
        ✨❤️✨✨❤️✨
        ✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨❤️❤️✨❤️❤️✨✨
        ✨❤️❤️❤️❤️❤️❤️❤️✨
        ✨❤️❤️❤️❤️❤️❤️❤️✨
        ✨✨❤️❤️❤️❤️❤️✨✨
        ✨✨✨❤️❤️❤️✨✨✨
        ✨✨✨✨❤️✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨💚💚✨💚💚✨✨
        ✨💚💚💚💚💚💚💚✨
        ✨💚💚💚💚💚💚💚✨
        ✨✨💚💚💚💚💚✨✨
        ✨✨✨💚💚💚✨✨✨
        ✨✨✨✨💚✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨💙💙✨💙💙✨✨
        ✨💙💙💙💙💙💙💙✨
        ✨💙💙💙💙💙💙💙✨
        ✨✨💙💙💙💙💙✨✨
        ✨✨✨💙💙💙✨✨✨
        ✨✨✨✨💙✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨💜💜✨💜💜✨✨
        ✨💜💜💜💜💜💜💜✨
        ✨💜💜💜💜💜💜💜✨
        ✨✨💜💜💜💜💜✨✨
        ✨✨✨💜💜💜✨✨✨
        ✨✨✨✨💜✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨🤍🤍✨🤍🤍✨✨
        ✨🤍🤍🤍🤍🤍🤍🤍✨
        ✨🤍🤍🤍🤍🤍🤍🤍✨
        ✨✨🤍🤍🤍🤍🤍✨✨
        ✨✨✨🤍🤍🤍✨✨✨
        ✨✨✨✨🤍✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨🖤🖤✨🖤🖤✨✨
        ✨🖤🖤🖤🖤🖤🖤🖤✨
        ✨🖤🖤🖤🖤🖤🖤🖤✨
        ✨✨🖤🖤🖤🖤🖤✨✨
        ✨✨✨🖤🖤🖤✨✨✨
        ✨✨✨✨🖤✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨💛💛✨💛💛✨✨
        ✨💛💛💛💛💛💛💛✨
        ✨💛💛💛💛💛💛💛✨
        ✨✨💛💛💛💛💛✨✨
        ✨✨✨💛💛💛✨✨✨
        ✨✨✨✨💛✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(time)
                msg.edit(f'''
        ✨✨✨✨✨✨✨✨✨
        ✨✨🧡🧡✨🧡🧡✨✨
        ✨🧡🧡🧡🧡🧡🧡🧡✨
        ✨🧡🧡🧡🧡🧡🧡🧡✨
        ✨✨🧡🧡🧡🧡🧡✨✨
        ✨✨✨🧡🧡🧡✨✨✨
        ✨✨✨✨🧡✨✨✨✨
        ✨✨✨✨✨✨✨✨✨''')
                sleep(3)
                
                
                msg.edit(f'<b>⭐ @ </b>')

        @app.on_message(filters.command("heart", prefixes=".") & filters.me)
        def betalove(_, msg):
            time = 0.6
            for i in range(1):
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
                sleep(time)
                msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
                sleep(1)
                
                
                
                



        textded11 = '''
                <b>спокойной ночи ,хуйня 🙃🙃</b>
                <b>спокойной ночи ,чмо 😟😟</b>
                <b>спокойной ночи ,аборт  💩</b>?
                <b>спокойной ночи ,уёбище 🙏</b>
                <b>спокойной ночи ,мразь 👰‍♀️👰‍♀️</b>
                <b>спокойной ночи ,днище  👷🏻  👷🏻 </b>
                <b>спокойной ночи ,прошмандовина  🖕🏼  🖕🏼 </b>
                <b>спокойной ночи ,скотина 👨🏼‍🚀</b>
                <b>спокойной ночи ,мордофиля 🏃🏼  🏃🏼 </b>
                <b>спокойной ночи ,безмамный(ая)  🤦🏿‍♀️ </b>
                <b>я</b>?
                <b> ебал </b>
                <b> твою </b>
                <b> мать </b>
                <b> вчера </b>
                '''


        @app.on_message(filters.command("night_osk", prefixes=".") & filters.me)
        def valentine(_, msg):
            txt = textded11.split("\n")
            e = True
            etime = int(msg.text.split('.night_osk ', maxsplit=1)[1])
            for i in txt:
                time = etime
                if e == True:
                    e = False
                elif time > 10:
                    try:
                        msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                        sleep(0.5)
                        msg.delete()
                    except:
                        pass
                else:
                    try:
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                        msg.edit(f'{i}')
                        sleep(time/6)
                    except:
                        pass
            msg.edit(f'<b> Это правда</b>')
            msg.edit(f'<b>⭐ У неё спроси </b>')
        @app.on_message(filters.command("ph", prefixes=".") & filters.me)
        def valentine(app, message):
            app.send_message(message.chat.id, f'<b>Скрипт года</b>')
            sleep(1)
            app.send_message(message.chat.id, f'<b>https://rt.pornhub.com</b>')
            sleep(1)
            app.send_message(message.chat.id, f'<b>https://rt.pornhub.com</b>')
            sleep(1)
            app.send_message(message.chat.id, f'<b>https://rt.pornhub.com</b>')
            sleep(1)

        @app.on_message(filters.command("toxic", prefixes=".") & filters.me)
        def valentine(app, message):
            app.send_message(message.chat.id,f'''
        <b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
        ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>пиздобратия мандопроушечная, уебище залупоглазое</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>гнидопаскудная хуемандовина</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>хуй тебе в глотку через анальный проход</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
            <b>гандон с гонореей...</b>
            ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>сортирующего яйца в пизде кастрированной кобылы</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>ебун хуеголовый, пидрасня ебаная. </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Залупоголовая блядоящерица. .</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Трипиздоблядская промудохуина! </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Облямуденный злоебучий страхопизднутый трихуемандаблядский </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>ебаквакнутый распиздаеб... </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Промудохуепиздамразоблядское злоепиздие </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Облямудевшая хуеблядина четырестохуйная</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>вестипёздная мразотоблядская шлюхасосалка. </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>блядь шмара козельуебок сдохни </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
             ''')
            sleep(0.5)
            app.send_message(message.chat.id, f'''
             <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
             ''')
            sleep(0.5)
            
            
            app.send_message(message.chat.id, f'''
             <b>⭐️ @</b>
             ''')





        


 


                
            

        jopa = '''
                   <b>ВЗЛОМ ЖОПЫ</b> 
                   <b><i>Loading...</i></b> 
            10%  █▒▒▒▒▒▒▒▒▒▒▒▒
            30%  ███▒▒▒▒▒▒▒▒▒▒    
            50%  █████▒▒▒▒▒▒▒▒
            66%  ██████▒▒▒▒▒▒▒
            79%  ████████▒▒▒▒▒
            84%  █████████▒▒▒▒
            89%  ██████████▒▒▒
            95%  ████████████▒
            99%  █████████████
            100% █████████████
            <b> ВАША ЖОПА ВЗЛОМАНА </b>
            <b><i>Создатель: "Прощайте"</i></b>
            <b><i>Создатель: "Прощайте"</i></b>
            <b><i>Создатель: "Прощайте"</i></b>
        '''
        zxc = '''
        <b>- All my friends are toxic, all ambitionless 💚</b>
        
        <b>- All my friends are toxic, all ambitionless 💜</b>
        
        <b>- All my friends are toxic, all ambitionless 💛</b>
        
        <b>- So rude and always negative 🤍</b>
        
        <b>- So rude and always negative 💚</b>
        
        <b>- So rude and always negative 💛</b>
        
        <b>- I need new friends, but it's not  that quick and easy 💔</b>
        
        <b>- I need new friends, but it's not  that quick and easy 💛</b>
        
        <b>- I need new friends, but it's not  that quick and easy 💚</b>
        
        <b>- Oh, I'm drowning, let me breathe 💜</b>
        
        <b>- Oh, I'm drowning, let me breathe 💛</b>
        
        <b>- Oh, I'm drowning, let me breathe 💛</b>
        
        '''


        love = '''
        🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
        <b>Загрузка любви...</b>
        ❤️🤍🤍🤍🤍🤍🤍🤍🤍🤍
        ❤️❤️🤍🤍🤍🤍🤍🤍🤍🤍
        ❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍
        ❤️❤️❤️❤️🤍🤍🤍🤍🤍🤍
        ❤️❤️❤️❤️❤️🤍🤍🤍🤍🤍
        ❤️❤️❤️❤️❤️❤️🤍🤍🤍🤍
        ❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍
        ❤️❤️❤️❤️❤️❤️❤️❤️🤍🤍
        ❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
        ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
        <b>Я люблю тебя ❤️‍🔥</b>
        <b>Я люблю тебя ❤️‍🔥</b>
        <b>Я люблю тебя ❤️‍🔥</b>
        <b>Я люблю тебя ❤️‍🔥</b>
        <b>Я люблю тебя ❤️‍🔥</b>
        
        '''

        comp = '''
        <b>Крошечные напоминания того, что ты...</b> 
        
        <b>Самая удивительная</b> ✨
        
        <b>Самая внимательная</b> ✨
        
        <b>Самая красивая</b> ✨
        
        <b>Самая успешная</b> ✨
        
        <b>Самая заботливая</b> ✨
        
        <b>Самая милая</b> ✨
        
        <b>Самая прекрасная</b> ✨
        
        <b>Самая умная</b> ✨
        
        <b>Самая шикарная</b> ✨
        
        <b>Самая обалденная ✨</b>
        
        <b>Самая очаровашка</b> ✨
        
        <b>Самая любимая</b> ✨
        
        <b>Самая весёлая</b> ✨
        
        <b>Самая нежная</b> ✨
        
        <b>Самая яркая</b> ✨
        
        <b>Самая прелестная</b> ✨
        
        <b>Самая приятная</b> ✨
        
        <b>Самая сладкая</b> ✨
        
        <b>Самая дивная</b> ✨
        
        <b>Самая ангельская</b> ✨
        
        <b>Самая добрая</b> ✨
        
        <b>Самая бесподобная</b> ✨
        
        <b>Самая волшебная</b> ✨
        
        <b>Самая лучшая</b> ✨
        
        <b>Самая крутышка</b> ✨
        
        <b>Самая аромтная</b> ✨
        
        <b>Самая единственная</b> ✨
        
        <b>Самая искренняя</b> ✨
        
        <b>Самая ласковая</b> ✨
        
        <b>Самая романтичная</b> ✨
        
        <b>Самая великолепная</b> ✨
        
        <b>Самая внимательная</b> ✨
        
        <b>Самая страстная</b> ✨
        
        <b>Самая игривая</b> ✨
        
        <b>Самая стройная</b> ✨
        
        <b>Самая безумная</b> ✨
        
        <b>Самая симпатичная</b> ✨
        
        <b>Самая изящная </b> ✨
        
        <b>Самая талантливая ✨</b>
        
        <b>Самая элегантная ✨</b>
        
        <b>Самая чуткая ✨</b>
        
        <b>Самая отзывчивая ✨</b>
        
        <b>Самая уникальная ✨</b>
        
        <b>Самая смелая ✨</b>
        
        <b>Самая уверенная ✨</b>
        
        <b>Самая особенная ✨</b>
        
        <b>Самая изумительная ✨</b>
        
        <b>Самая настоящая ✨</b>
        
        <b>Самая обаятельная ✨</b>
        
        <b>Самая пушистая ✨</b>
        
        <b>Самая кокетливая ✨</b>
        
        <b>Самая теплая ✨</b>
        
        <b>Самая энергичная ✨</b>
        
        <b>Самая неотразимая ✨</b>
        
        <b>Самая неописуемая ✨</b>
        
        <b>Самая грациозная ✨</b>
        
        <b>Самая сказочная ✨</b>
        
        <b>Самая желанная ✨</b>
        
        <b>Самая изысканная ✨</b>
        
        <b>Самая мечтательная ✨</b>
        
        <b>Самая безупречная ✨</b>
        
        <b>Самая совершеная ✨</b>
        
        <b>Самая честная ✨</b>
        
        <b>Самая улыбчивая ✨</b>
        
        <b>Самая ненаглядная ✨</b>
        
        <b>Самая женственная ✨</b>
        
        <b>Самая цветущая ✨</b>
        
        <b>Самая гармоничная ✨</b>
        
        <b>Самая отрадная ✨</b>
        '''

        ziga = '''
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍❤️❤️❤️🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍❤️❤️❤️❤️❤️🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍❤️❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️❤️🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍❤️❤️❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️❤️❤️🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🧡🧡🧡🧡🤍🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🤍🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🧡🧡🧡🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🤍🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🤍🧡🧡🧡🧡🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💛💛💛💛🤍💛💛🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍🤍🤍🤍💛🤍🤍💛🤍
        🤍💛💛💛💛💛💛💛🤍
        🤍💛🤍🤍💛🤍🤍🤍🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍💛💛🤍💛💛💛💛🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💚💚💚💚🤍💚💚🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍🤍🤍🤍💚🤍🤍💚🤍
        🤍💚💚💚💚💚💚💚🤍
        🤍💚🤍🤍💚🤍🤍🤍🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍💚💚🤍💚💚💚💚🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💙💙💙💙🤍💙💙🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍🤍🤍🤍💙🤍🤍💙🤍
        🤍💙💙💙💙💙💙💙🤍
        🤍💙🤍🤍💙🤍🤍🤍🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍💙💙🤍💙💙💙💙🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💜💜💜💜🤍💜💜🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍🤍🤍🤍💜🤍🤍💜🤍
        🤍💜💜💜💜💜💜💜🤍
        🤍💜🤍🤍💜🤍🤍🤍🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍💜💜🤍💜💜💜💜🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🧡🧡🧡🧡🤍🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🤍🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🧡🧡🧡🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🤍🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🤍🧡🧡🧡🧡🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💛💛💛💛🤍💛💛🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍🤍🤍🤍💛🤍🤍💛🤍
        🤍💛💛💛💛💛💛💛🤍
        🤍💛🤍🤍💛🤍🤍🤍🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍💛💛🤍💛💛💛💛🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💚💚💚💚🤍💚💚🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍🤍🤍🤍💚🤍🤍💚🤍
        🤍💚💚💚💚💚💚💚🤍
        🤍💚🤍🤍💚🤍🤍🤍🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍💚💚🤍💚💚💚💚🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💙💙💙💙🤍💙💙🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍🤍🤍🤍💙🤍🤍💙🤍
        🤍💙💙💙💙💙💙💙🤍
        🤍💙🤍🤍💙🤍🤍🤍🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍💙💙🤍💙💙💙💙🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💜💜💜💜🤍💜💜🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍🤍🤍🤍💜🤍🤍💜🤍
        🤍💜💜💜💜💜💜💜🤍
        🤍💜🤍🤍💜🤍🤍🤍🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍💜💜🤍💜💜💜💜🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🧡🧡🧡🧡🤍🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🤍🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🧡🧡🧡🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🤍🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🤍🧡🧡🧡🧡🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💛💛💛💛🤍💛💛🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍🤍🤍🤍💛🤍🤍💛🤍
        🤍💛💛💛💛💛💛💛🤍
        🤍💛🤍🤍💛🤍🤍🤍🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍💛💛🤍💛💛💛💛🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💚💚💚💚🤍💚💚🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍🤍🤍🤍💚🤍🤍💚🤍
        🤍💚💚💚💚💚💚💚🤍
        🤍💚🤍🤍💚🤍🤍🤍🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍💚💚🤍💚💚💚💚🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💙💙💙💙🤍💙💙🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍🤍🤍🤍💙🤍🤍💙🤍
        🤍💙💙💙💙💙💙💙🤍
        🤍💙🤍🤍💙🤍🤍🤍🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍💙💙🤍💙💙💙💙🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💜💜💜💜🤍💜💜🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍🤍🤍🤍💜🤍🤍💜🤍
        🤍💜💜💜💜💜💜💜🤍
        🤍💜🤍🤍💜🤍🤍🤍🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍💜💜🤍💜💜💜💜🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🧡🧡🧡🧡🤍🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🤍🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🧡🧡🧡🧡🧡🤍
        🤍🧡🤍🤍🧡🤍🤍🤍🤍
        🤍🧡🤍🤍🧡🤍🤍🧡🤍
        🤍🧡🧡🤍🧡🧡🧡🧡🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💛💛💛💛🤍💛💛🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍🤍🤍🤍💛🤍🤍💛🤍
        🤍💛💛💛💛💛💛💛🤍
        🤍💛🤍🤍💛🤍🤍🤍🤍
        🤍💛🤍🤍💛🤍🤍💛🤍
        🤍💛💛🤍💛💛💛💛🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💚💚💚💚🤍💚💚🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍🤍🤍🤍💚🤍🤍💚🤍
        🤍💚💚💚💚💚💚💚🤍
        🤍💚🤍🤍💚🤍🤍🤍🤍
        🤍💚🤍🤍💚🤍🤍💚🤍
        🤍💚💚🤍💚💚💚💚🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💙💙💙💙🤍💙💙🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍🤍🤍🤍💙🤍🤍💙🤍
        🤍💙💙💙💙💙💙💙🤍
        🤍💙🤍🤍💙🤍🤍🤍🤍
        🤍💙🤍🤍💙🤍🤍💙🤍
        🤍💙💙🤍💙💙💙💙🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍💜💜💜💜🤍💜💜🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍🤍🤍🤍💜🤍🤍💜🤍
        🤍💜💜💜💜💜💜💜🤍
        🤍💜🤍🤍💜🤍🤍🤍🤍
        🤍💜🤍🤍💜🤍🤍💜🤍
        🤍💜💜🤍💜💜💜💜🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍❤️❤️❤️❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️❤️❤️❤️🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍❤️❤️❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️❤️❤️🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍❤️❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍❤️🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍❤️🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️❤️🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍❤️❤️❤️❤️❤️❤️❤️🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍❤️❤️❤️❤️❤️🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍❤️❤️❤️🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍❤️🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        🤍🤍🤍🤍🤍🤍🤍🤍🤍
        '''

        redss = f'''🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️
⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️
⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️⚫️
СЛАВА УКРАЇН!
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
ГЕРОЯМ СЛАВА!
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟨🟦🟦🟦🟦🟨🟦🟦🟦🟦🟨🟦
🟦🟨🟨🟦🟦🟨🟨🟨🟦🟦🟨🟨🟦
🟦🟨🟦🟨🟦🟨🟨🟨🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟨🟨🟨🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟨🟦🟦🟨🟨🟨🟦🟦🟨🟨🟦
🟦🟨🟦🟨🟨🟦🟦🟦🟨🟨🟦🟨🟦
🟦🟨🟦🟦🟨🟨🟦🟨🟨🟦🟦🟨🟦
🟦🟨🟦🟦🟨🟦🟨🟦🟨🟦🟦🟨🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟦🟦🟦🟦🟨🟨🟨🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟨🟦🟦🟦🟦🟦🟦
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
СЛАВА ЗСУ!
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
СЛАВА АЗОВУ!
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟨🟦🟦🟦🟦🟦🟦🟦🟦⬛️🟦🟨🟦
🟦🟨🟦⬛️🟦🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦🟦⬛️🟦🟨🟦
🟦🟨🟦⬛️🟦🟦🟦🟦🟦🟦🟦🟦🟨🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
РОСІЯ ВЖЕ ПРОГОРАЛА ВІЙНУ!
💙💙💙💙💙💙
💙💙💙💙💙💙
💙💙💙💙💙💙
💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛💛💛💛💛
СЛАВА УКРАЇНІ!
ГЕРОЯМ СЛАВА!
🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴
⚫️⚫️⚫️⚫️⚫️⚫️
⚫️⚫️⚫️⚫️⚫️⚫️
⚫️⚫️⚫️⚫️⚫️⚫️
СЛАВА УКРАЇН!
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
ГЕРОЯМ СЛАВА!
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟨🟦🟦🟦🟦🟨🟦🟦🟦🟦🟨🟦
🟦🟨🟨🟦🟦🟨🟨🟨🟦🟦🟨🟨🟦
🟦🟨🟦🟨🟦🟨🟨🟨🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟨🟨🟨🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟨🟦🟦🟨🟨🟨🟦🟦🟨🟨🟦
🟦🟨🟦🟨🟨🟦🟦🟦🟨🟨🟦🟨🟦
🟦🟨🟦🟦🟨🟨🟦🟨🟨🟦🟦🟨🟦
🟦🟨🟦🟦🟨🟦🟨🟦🟨🟦🟦🟨🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟦🟦🟦🟦🟨🟨🟨🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟨🟦🟦🟦🟦🟦🟦
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
СЛАВА ЗСУ!
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
СЛАВА АЗОВУ!
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟨🟦🟦🟦🟦🟦🟦🟦🟦⬛️🟦🟨🟦
🟦🟨🟦⬛️🟦🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦🟦⬛️🟦🟨🟦
🟦🟨🟦⬛️🟦🟦🟦🟦🟦🟦🟦🟦🟨🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
РОСІЯ ВЖЕ ПРОГОРАЛА ВІЙНУ!
💙💙💙💙💙💙
💙💙💙💙💙💙
💙💙💙💙💙💙
💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛💛💛💛💛
СЛАВА УКРАЇНІ!
ГЕРОЯМ СЛАВА!
🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴
⚫️⚫️⚫️⚫️⚫️⚫️
⚫️⚫️⚫️⚫️⚫️⚫️
⚫️⚫️⚫️⚫️⚫️⚫️
СЛАВА УКРАЇН!
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
ГЕРОЯМ СЛАВА!
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟨🟦🟦🟦🟦🟨🟦🟦🟦🟦🟨🟦
🟦🟨🟨🟦🟦🟨🟨🟨🟦🟦🟨🟨🟦
🟦🟨🟦🟨🟦🟨🟨🟨🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟨🟨🟨🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟦🟨🟦🟦🟨🟦🟦🟨🟦🟨🟦
🟦🟨🟨🟦🟦🟨🟨🟨🟦🟦🟨🟨🟦
🟦🟨🟦🟨🟨🟦🟦🟦🟨🟨🟦🟨🟦
🟦🟨🟦🟦🟨🟨🟦🟨🟨🟦🟦🟨🟦
🟦🟨🟦🟦🟨🟦🟨🟦🟨🟦🟦🟨🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟦🟦🟦🟦🟨🟨🟨🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟨🟦🟦🟦🟦🟦🟦
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
СЛАВА ЗСУ!
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
СЛАВА АЗОВУ!
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟨🟦🟦🟦🟦🟦🟦🟦🟦⬛️🟦🟨🟦
🟦🟨🟦⬛️🟦🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️⬛️⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️⬛️⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦⬛️⬛️🟦🟨🟦
🟦🟨🟦⬛️⬛️🟦⬛️⬛️🟦🟦⬛️🟦🟨🟦
🟦🟨🟦⬛️🟦🟦🟦🟦🟦🟦🟦🟦🟨🟦
🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦🇺🇦
РОСІЯ ВЖЕ ПРОГРАЛА ВІЙНУ!
💙💙💙💙💙💙
💙💙💙💙💙💙
💙💙💙💙💙💙
💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛💛💛💛💛
СЛАВА УКРАЇНІ!
ГЕРОЯМ СЛАВА!'''
        
        app.run()
    else:
        print("Ошибка,ваш айди не найден в базе.!")
        print("Свяжитесь с  @Nex1n_dev в Telegram. Ваш HWID: " + hwid)
        os.system('pause >NUL')

check_hardware_hwid()