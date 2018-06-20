from urllib import request
import  re


# 1. 爬取豆瓣电影名称和星级评价



def douban(html):
  print(html)

def getHtml(url):
    response=request.urlopen(url)
    html=response.read();
    html = html.decode('utf-8');
    return  html;
def sub(html):

    s1='<div class="review-list chart ">';
    e1='<div class="paginator">';
    start=html.find(s1,1)
    end=html.find(e1,1);
    htmldivinfo=html[start:end]

    ###################title#######################
    reg='<h2>.*</h2>';
    pattern=re.compile(reg);
    h2list=re.findall(pattern,htmldivinfo);
    for row in h2list:
        s1=row.find('">',1);
        e2=row.find('</a',1);
        row=row[s1+2:e2]
        print(row);
    ###################imgurl#####################
    regurl="<(?i)img alt(.*?)/?>";
    pattern = re.compile(regurl);
    imgurl = re.findall(pattern, htmldivinfo);
    for url in imgurl:
        print(url);
    ##################star level#########################
    regstar='<span property="v:rating".*</span>';
    pattern = re.compile(regstar);
    star_level = re.findall(pattern, htmldivinfo);
    for star in star_level:
        print(star)

print("OK")
url="https://movie.douban.com/review/best/?start=10";
html=getHtml(url)
sub(html);



