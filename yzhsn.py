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

warnings.simplefilter("ignore", UnicodeWarning)##UnicodeWarningを黙らせます
"""
このスクリプトを動かすには、別途mastodonモジュールとpyscreenshotモジュールが必要だよ。
どっちもpipで入れられるから、インストールしてから動かしてね。
ログイントークンは事前に取得しておいてね。
"""
def login():
    mastodon = Mastodon(client_id="credtest.txt",access_token="clientcred.txt",api_base_url = "https://friends.nico")
    return mastodon


class main(StreamListener):
    def __init__(self):
        self.status = status
        self.account = status["account"]
        self.g_vis = "public"
        self.in_reply_to_id = None
        self.media_files = None

    def cp():
        account = status["account"]
        tl = mastodon.timeline_home(limit=0)
        listener = MstdnStreamListner()
        stream = MstdnStream('api_base_url', 'access_token', listener)
        stream.timeline_home()
        if account["acct"] == "アカウントID":
            if status
                im = ImageGrab.grab()
                im.save('screenshot.png')#スクショ取るよ

    

if __name__ == '__main__':
    main()
