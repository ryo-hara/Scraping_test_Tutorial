# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup

def scraping():
    url = "https://news.yahoo.co.jp/topics"
    response = requests.get(url)
    response.status_code

    bs = BeautifulSoup(response.content,"lxml")

    print(bs.select('a')[0])

    topics = bs.select('.fl, .fr')
    print(topics[0])

    print(topics[0].select('li')[0].text)

    news_topics = {}
    for news in topics:
        topic = news.select('li')[0].text
        news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

    print('終了')

    topics_dt = pd.DataFrame.from_dict(news_topics)
    topics_dt.apply( lambda x: x.str.replace(r'(new|写真|動画)',''))
    print('scraping終了')
    #topics_dt.to_csv( "oppai.csv" )

    return 0


scraping()
