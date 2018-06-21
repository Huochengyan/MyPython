import requests
from pyquery import PyQuery as pq

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
    doc=pq(html)
    print(doc.find('div[class="z"] a')[0].text)
    print(doc.find('div[class="z"] a')[1].text)
