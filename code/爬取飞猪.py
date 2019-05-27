import requests
from requests.exceptions import RequestException
import pymongo
import pandas as pd
def get_one_page(url):
    try:
        headers = {
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }
        respone = requests.get(url, headers = headers)
        if respone.status_code == 200:
            return respone.json()
        return None
    except RequestException:
        return None
def parse_one_page(html, city):
    data_list = html['data']['data'].get('itemProducts')['data']['list'][0]['auctions']
    for data in data_list:
        data['city'] = city
        yield data

def save_to_mongo(item):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.Laborday
    collection = db.items
    collection.insert_one(item)



def main():
    cities = list(pd.read_csv('../data/city_data.csv')['city'])
    for city in cities:
        url = 'https://travelsearch.fliggy.com/async/queryItemResult.do?spm=181.61408.a1z7d.6.2c1523e4XpBvMM&searchType=product&keyword=%s&category=SCENIC&ttid=sem.000000736&pagenum={}'%str(city)
        html = get_one_page(url.format('1'))
        itemPagenum = html['data']['data'].get('itemPagenum')
        if itemPagenum is not None:
            page_count = itemPagenum['data']['count']
            for page in range(1, page_count+1):
                html = get_one_page(url.format(page))
                items = parse_one_page(html, city)
                for item in items:
                    save_to_mongo(item)


main()