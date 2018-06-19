import  os,bs4
import  requests

os.makedirs("mytest",exist_ok=True)

"""
要爬去的页面https://xkcd.com/ 中的图片
"""
url="https://xkcd.com"
html=requests.get(url).text;
soup=bs4.BeautifulSoup(html,'lxml')
imglist=soup.select('#comic img')
if imglist==[]:
    print("未能找到图片元素！！")
else:
    for img in imglist:
        url=url+img.get('src')
        res=requests.get(url)
        imgfilepath=open(os.path.join("mytest",os.path.basename(url)),'wb')
        for imgs in res.iter_content(1000):
            imgfilepath.write(imgs)
        imgfilepath.close();

