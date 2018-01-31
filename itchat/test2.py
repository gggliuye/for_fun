# -*- coding: gb2312 -*-
import itchat
import random
from itchat.content import *

default = ['恩啊','好的','恩恩','哈哈','[害羞]','[奸笑]']
"""
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg.User.NickName,':', msg.Text)
    return default[random.randint(1,5)]
"""

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    print(msg)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return 

itchat.auto_login(hotReload=True)
itchat.run()