import  os,bs4,requests
import lxml
from DB import SqliteDBHelper

# -*- coding: utf-8 -*-

from DBHelper import DBHelper
from Model.DouBanMoiveInfo import DouBanMoiveInfo

#使用代理  爬取豆瓣数据保存到数据库

# 根据协议类型，选择不同的代理
proxies = {
  "https": "122.72.18.35:80",
  "https": "101.132.122.230:3128",
}


os.makedirs("DouBan",exist_ok=True)
url="https://movie.douban.com/review/best/?start=10";

httpcode=200;
startindex=10
while(httpcode==200):

    # try:
    #     requests.get('https://movie.douban.com/review/best/?start=10', proxies=proxies)
    # except:
    #     print('connect failed')
    #     break;
    # else:
    #     print( 'success')

    res=requests.get(url)
    html=res.text;
    soup=bs4.BeautifulSoup(html,'lxml')
    divlist=soup.select('div[class="review-list chart "] div[class="main review-item"]')
    if(divlist==[]):
        print("未能找到div列表")
    sqlList=[];
    infoList=[];
    for divstr in divlist:
        img=divstr.select('img[rel="v:image"]');
        if(img!=[]):
                img=img[0]
                if(img.get("title")!=""and img.get("src")!=""):
                     info= DouBanMoiveInfo(0,img.get("title"),img.get('src'))  # 留待入库
                     res=requests.get(info.imgUrl)
                     if(res.status_code==200):
                         httpcode=200
                     imgpath=open(os.path.join("DouBan",os.path.basename(info.imgUrl)),'wb')
                     for imgs in res.iter_content(1000):
                         imgpath.write(imgs);
                     imgpath.close()
                     sql="INSERT INTO `douban` (`moiveName`, `imgurl`) VALUES ('"+info.moiveName+"','"+info.imgUrl+"');"
                     sqlList.append(sql);
                     infoList.append(info)

    url="https://movie.douban.com/review/best/?start="+str(startindex)
    print(url)
    if(startindex>10):
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
