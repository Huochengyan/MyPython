import os,bs4

import requests

"""
1. 本地保存 2.数据库保存
"""

url="https://xkcd.com/";
#创建文件夹
os.makedirs('xkcd',exist_ok=True)

while not url.endswith("#"):
    #print("下载图片网址",url)
    res=requests.get(url)
    res.raise_for_status()
   # print(res.text)
    """
    1.得到网站 2. 解析
    """
    soup=bs4.BeautifulSoup(res.text,'lxml')
    # 搜索 文档书
    comicImg=soup.select("#comic img")
    if comicImg==[]:
        print("没有找到漫画对象！！")
    else:
        comicUrl='https:'+comicImg[0].get('src')
        print("下载图片路径%s...",comicUrl)
        res=requests.get(comicUrl)
        res.raise_for_status()
        #bsetname  只保留路径的最后一个元素
        # os.path.basename(comicUrl)) 只保留路径的最后一个元素
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        print(imageFile)
        #指定每次下载获取元素
        for imgs in res.iter_content(1000):
            #把每次遍历的文件写入文件夹目录里
            imageFile.write(imgs)
        imageFile.close();
    #获取上一页url
    prevLink=soup.select('a["rel="prev""]')[0]
    url="https://xkcd.com/"+prevLink.get("href")
    print(url)

print("数据采集完成！！！")




