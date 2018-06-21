import  os,bs4,requests
import lxml
from DB import SqliteDBHelper

proxies = {
  "https": "122.72.18.35:80",
  "https": "101.132.122.230:3128",
}

url="https://www.ruyile.com/school/r78147/";

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
    divList=soup.select('div[class="z"] a')
    if(divList==[]):
        print("未能找到trlist列表")
    print(divList[0].next_element)
    print(divList[1].next_element)

