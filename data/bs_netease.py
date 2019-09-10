# -*- coding: UTF-8 -*-

import requests, json, re
from bs4 import BeautifulSoup
from pymongo import MongoClient

def getUrlsFromJs(url, label, page):
    print(url)
    urlStr = url + '0{}.js'
    url_list = []
    for i in range(1, page + 1):
        getUrl = urlStr.format(i)
        r = requests.get(getUrl)
        if r.status_code != 200:
            continue
        r.encoding = 'gb2312'
        content = json.loads(str(r.text)[14:-1])
        url_list += [(i['docurl'], i['keywords'], i['imgurl'], label) for (index,i) in enumerate(content)]
    return url_list

def getDetailFromUrl(url, keywords, imgurl, label):
    resp = requests.get(url)
    res = {}
    if resp.status_code == 200:
        try:
            soup = BeautifulSoup(resp.text, 'html.parser')
            title = soup.find('h1')
            if title:
                title = title.get_text() # title
            else:
                title = soup.find('h2').get_text()
            content = soup.find(id='endText')
            scripts = content.find_all('script')
            content_clean = str(content)
            for i in scripts:
                content_clean = content_clean.replace(str(i), '') # content
            source = content.find(class_='ep-source').find_all('span')[0].text
            source_from = source.strip() # source
            time = soup.find(class_ = 'post_time_source').get_text().split('　')[0].strip() # time
            res = {
                'title': title,
                'content': content_clean,
                'source': source_from,
                'publish_time': time,
                'keywords': keywords,
                'imgurl': imgurl,
                'label': label
            }
            setDataInDB(res)
        except Exception:
            res = {}
            print('格式错误')
    return res

def setDataInDB(data):
    client = MongoClient('mongodb://localhost:27017')
    client.admin.authenticate("admin", "123321")
    db = client.admin
    if len(data.items()) > 0:
        news_db = db.news
        test_id = news_db.insert_one(data).inserted_id
        print(test_id)

if __name__ == '__main__':
    js = [
        'https://temp.163.com/special/00804KVA/cm_yaowen_',
        'https://temp.163.com/special/00804KVA/cm_guonei_', 
        'https://temp.163.com/special/00804KVA/cm_guoji_', 
        'https://temp.163.com/special/00804KVA/cm_war_',
        'https://temp.163.com/special/00804KVA/cm_money_',
        'https://temp.163.com/special/00804KVA/cm_tech_'
    ]
    labels = ['要闻', '国内', '国际', '军事', '财经', '科技']
    urls = []
    for (j, l) in zip(js, labels):
        urls += getUrlsFromJs(j, l, 10)
    for (url, keywords, imgurl, label) in urls:
        getDetailFromUrl(url, keywords, imgurl, label)
        print(url)
