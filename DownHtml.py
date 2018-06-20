import urllib
from urllib import request
import re

import os

print("hello world")

def getHtml(url):
    response = request.urlopen(url)
    html = response.read();
    return  html
def getImg(html):
    html=html.decode('utf-8');
    reg = r'http.*?.jpg'  # 正则表达式，得到图片地址
    pattern1 = re.compile(reg)  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist=re.findall(pattern1,html)
    x=0
    dir='D:\E1\F1';
    for imgurl in imglist:
        try:
         if not os.path.isdir(dir):
             os.makedirs(dir)
         urllib.request.urlretrieve(imgurl, dir+'%s.jpg' % x)
         x += 1
        except Exception as err:
          print(err)
html=getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0")
print(getImg(html))