import  requests,bs4,json


"""

登录脉脉爬取自己的好友信息

"""

def login():
    session=requests.session()
    login_data={
        'm':'13718562199',
        'p':'929914120.huo',
        'to':'https://maimai.cn/im/',
        'pa':'+86'
    }
    session.post('https://acc.maimai.cn/login',data=login_data)
    res=session.get('https://maimai.cn/im/')
    res.encoding = 'utf-8'
    #html=res.text.encode('unicode_escape');
    #soup=bs4.BeautifulSoup(html,'lxml')

    #请求用户信息
    resInfo=session.get("https://maimai.cn/im/")
    datainfo=res.text.encode('unicode_escape');
    datainfo=datainfo.decode('utf-8')
    #截取Json
    start1Str='JSON.parse("'
    start1=datainfo.find(start1Str)
    end1=datainfo.find('");</script>')
    jsondata=datainfo[start1+start1Str.__len__():end1]
    jsondata=jsondata.replace(r"\\u",r'\u')

    #unicode码 转中文
    jsondata=jsondata.encode('utf-8').decode('unicode_escape')
    jsonObj=json.loads(jsondata)
    print(jsonObj)
    access_token=jsonObj['auth_info']['access_token']
    contactUrl='https://open.taou.com/maimai/contact/v4/pbd1?' \
               'version=4.0.0' \
               '&ver_code=web_1' \
               '&channel=www' \
               '&push_permit=1' \
               '&u=5101270' \
               '&_csrf=YybU6noU-pJ7b3UqvGzxthkSf-D-qxsHZGbo' \
               '&access_token='+access_token+'' \
               '&uid=%226Rj6oBS5M5%2BwNjnPzgbCJ%2FAirs3A3wL6ApgZu%2Fo1crA%3D%22' \
               '&token=%22vIr%2FvMW18VW1fKIgUw4ZjEl8h1ORsiXA5HH%2B96xykc3BL6lviTac87F8euVE%2BNkh8CKuzcDfAvoCmBm7%2BjVysA%3D%3D%22' \
               '&json=1' \
               '&paginate=0'

    res=session.get(contactUrl);
    print(res.text);

login()