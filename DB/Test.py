import  os,bs4,requests
import lxml
from DB import SqliteDBHelper

# -*- coding: utf-8 -*-

from DBHelper import DBHelper
from Model.DouBanMoiveInfo import DouBanMoiveInfo

#使用代理  爬取豆瓣数据保存到数据库

# 根据协议类型，选择不同的代理
proxies = {
  "http": "111.155.116.223:8123",
  "http": "112.115.57.20:3128",
}


os.makedirs("DouBan",exist_ok=True)
url="https://movie.douban.com/review/best/?start=10";

httpcode=200;
startindex=10
while(httpcode==200):

    try:
        requests.get('https://movie.douban.com/review/best/?start=10', proxies=proxies)
    except:
        print('connect failed')
        break;
    else:
        print( 'success')

    res=requests.get(url, proxies=proxies)
    html=res.text;
    soup=bs4.BeautifulSoup(html,'lxml')
    divlist=soup.select('div[class="review-list chart "] div[class="main review-item"]')
    if(divlist==[]):
        print("未能找到div列表")
    sqlList=[];
    infoList=[];
    for divstr in divlist:
        img=divstr.select('img[rel="v:image"]');
        span=divstr.select('span[property="v:rating"]');
        if(img!=[]):
                img=img[0]
                title='',
                star=''
                if(span!=[]):
                    span=span[0]
                    title=span.get('title');                       # 获得综合评价
                    star=span.get('class')[0].split('allstar')[1]  # 获得星级
                    print(title,star)
                if(img.get("title")!=""and img.get("src")!=""):
                     info= DouBanMoiveInfo(0,img.get("title"),img.get('src'))  # 留待入库
                     res=requests.get(info.imgUrl)
                     if(res.status_code==200):
                         httpcode=200
                     imgpath=open(os.path.join("DouBan",os.path.basename(info.imgUrl)),'wb')
                     for imgs in res.iter_content(1000):
                         imgpath.write(imgs);
                     imgpath.close()
                     sql="INSERT INTO `douban` (`moiveName`, `imgurl`,`title`, `star`) VALUES ('"+info.moiveName+"','"+info.imgUrl+"','"+title+"','"+star+"');"
                     sqlList.append(sql);
                     infoList.append(info)

    url="https://movie.douban.com/review/best/?start="+str(startindex)
    if(startindex>500):
        break;

    startindex = startindex + 10;
    for sql in sqlList:
        print(sql)
        result = SqliteDBHelper.SqliteDBHelper.ExSql(SqliteDBHelper, sql);
        print(result.rowcount)
print("OK 10 items")
for info in infoList:
    print(info.imgUrl)
print(infoList.__len__())
