#coding=utf-8
from aip import AipOcr

import re

#百度文字识别
# !/usr/bin/env python
# -*- coding:utf-8 -*-

import ConfigParser
import os

os.chdir("E:\python_project\Asktao_Automation\util")

cf = ConfigParser.ConfigParser()

# cf.read("test.ini")
cf.read("config.ini")

#return all section
secs = cf.sections()

APPP_ID = cf.get("baiduAip","APPP_ID")
API_KEY = cf.get("baiduAip","API_KEY")
SECRET_KEY = cf.get("baiduAip","SECRET_KEY")

# print "APPP_ID:", APPP_ID
# print "API_KEY:", API_KEY
# print "SECRET_KEY:", SECRET_KEY

client = AipOcr(APPP_ID,API_KEY,SECRET_KEY)

def characterRecognition(filePath):
    i = open(filePath,'rb')

    img = i.read()

    message = client.basicGeneral(img);

    #print(message.get('words_result'))
    string = '';

    for i in message.get('words_result'):

        print(i.get('words'))
        string += i.get('words')
    return string