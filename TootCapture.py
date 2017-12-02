# -*- coding: utf-8 -*-

from mastodon import *
import re, sys, os, csv, json, codecs, io
import threading, requests, random
from datetime import datetime
from pytz import timezone
from xml.sax.saxutils import unescape as unesc
import warnings, traceback
from PIL import ImageGrab
from stream import MstdnStream, MstdnStreamListner

warnings.simplefilter("ignore", UnicodeWarning)##UnicodeWarningを黙らせます(　◜◡‾)
"""
このスクリプトを動かすには、別途mastodonモジュールとpyscreenshotモジュールが必要だよ。
どっちもpipで入れられるから、インストールしてから動かしてね。
ログイントークンは事前に取得しておいてね。
"""
def login():
    mastodon = Mastodon(client_id="credtest.txt",access_token="clientcred.txt",api_base_url = "https://friends.nico")#インスタンスは変更可
    return mastodon


class main(StreamListener):
    def on_update(self, status):
        account = status["account"]
        if account["acct"] == "アカウントID":
            if status#ここでトゥートの非公開を判別してスクショ取るはずなんですが。まだ作りかけです＞＜
                im = ImageGrab.grab()
                im.save('screenshot.png')#スクショ取るよ

 class bot():
    def t_user():
        try:
            listener = main()
            mastodon.user_stream(listener)
         except:
            pass

if __name__ == '__main__':
    login()
    l = threading.Thread(target=bot.t_user)
    l.start()
