#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re  # 这个库导入是为了使用正则表达式读取读取找到的内容中的数字

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
number = ['']  # 用于储存读到的数字

while True:
    content = urllib.request.urlopen(
        url + number[0])  # number为字符串，number[0]为数字
    bs_obj = BeautifulSoup(content, "html.parser")  # html.parser表示解析网站，不返回任何值
    number = bs_obj.h3.string  # 网页显示出的“你需要在网址后输入数字44513”在html的h3 tag中，number在这里读出了h3里面的内容
    number = re.findall(r'\d+', number)  # 读出了number里面的数字
    if not number:  # 必须判断页面中还有是否还有number，没有说明已经到了最后一个页面，这时应该跳出循环，打印 bs_obj.h3.string
        break
    else:
        print(number[0])
print(bs_obj.h3.string)
