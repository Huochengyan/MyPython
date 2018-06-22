import  os,bs4,requests

"""
天气
"""
url="http://www.tianqihoubao.com/";
res=requests.get(url)
soup=bs4.BeautifulSoup(res.text,'lxml')
alist=soup.select('div[id="content"] a');

i=0;
for a in alist:
    detalisUrl=url+a.get('href')
    details=requests.get(detalisUrl)
    cityList = soup.select('div[id="content"] a');
    for  city in cityList:
        cityUrl=url+a.get('href')
        weatherHtml=bs4.BeautifulSoup(requests.get(cityUrl).text.encode('utf-8'),'lxml')
        trList=weatherHtml.select('table')[0].select('tr')[2:]
        for tr in trList:
            citytd=tr.select('td');
            for td in  citytd:
                cityName=td.select('a')[0].next_element;
                weatherUrl=url+'weather/'+td.select('a')[0].get('href')
                print('city:',cityName,weatherUrl)
                weatherInfoDetails=bs4.BeautifulSoup(requests.get(weatherUrl).text.encode('utf-8'),'lxml')
                tr2List=weatherInfoDetails.select('table')[0].select('tr')[2:]
                for tr in tr2List:
                    tdList=tr.select('td');
                    i = i + 1
                    print(str(i)+':',tdList[0].next_element,tdList[1].select('a')[0].next_element,tdList[2].next_element,tdList[3].next_element,tdList[4].next_element,tdList[5].next_element,tdList[6].next_element,tdList[7].next_element)
 #                    sql='INSERT INTO "weather" ("province","city","date","day_weather","day_wind","day_temperature","night_weather","night_wind","night__temperature")VALUES(' \
 #                         '"+tdList[0].next_element+",' \
 #                         '"+tdList[0].next_element+",' \
 #                        '"+tdList[0].next_element+",' \
 # \
 #                        '	);'

