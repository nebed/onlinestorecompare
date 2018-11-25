import os

import requests
import re
import json
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request
from store_functions import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

JUMIA_URL = os.getenv('JUMIA_URL', 'https://www.jumia.com.ng/catalog/?q=')
KONGA_URL = os.getenv('KONGA_URL', 'https://b9zcrrrvom-3.algolianet.com/1/indexes/*/queries')
KARA_URL = os.getenv('KARA_URL', 'http://www.kara.com.ng/catalogsearch/result?q=')
SLOT_URL = os.getenv('SLOT_URL', 'https://slot.ng/?post_type=product&s=')
EMPTY_LIST = []

urls = [JUMIA_URL,KONGA_URL,KARA_URL,SLOT_URL]


@app.route('/')
def hello_world():
	return render_template('index.html'),200

@app.route('/search/<term>/', methods=['GET'])
def search_products(term=None):
    '''
    Searches online stores using the given term. If no term is given, defaults to recent.
    '''
    #sort_arg = sort_filters[request.args.get('sort')] if sort in sort_filters else ''

    jumiaurl = JUMIA_URL + re.sub(r"\s+", '+', str(term))
    #kongaurl = KONGA_URL + re.sub(r"\s+", '%20', str(term))
    karaurl = KARA_URL + str(term)
    sloturl = SLOT_URL + str(term)
    #jumiaresult=parse_jumia(jumiaurl)
    #kararesult=parse_kara(karaurl)
    kongaresult=parse_konga(KONGA_URL,term)
    #slotresult=parse_slot(sloturl)

    return jsonify(kongaresult), 200

def parse_jumia(url, sort=None):
    '''
    This function parses the page and returns list of torrents
    '''
    print(url)
    STORE = "jumia"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('section', {'class': 'products -mabaya'})
    if table_present is None:
        return EMPTY_LIST
    titles = parse_titles(soup,STORE)
    images = parse_images(soup,STORE)
    prices = parse_prices(soup,STORE)
    #ratings = parse_ratings(soup,STORE)
    product_urls = parse_product_urls(soup,STORE)
    #price_drops = parse_price_drops(soup,STORE)
    search_results = []
    for search_result in zip(titles, images, prices, product_urls):
        search_results.append({
            'title': search_result[0],
            'image': search_result[1],
            'price': search_result[2],
            'url': search_result[3],
        })
    '''for search_result in zip(titles, images, prices, ratings, product_urls, price_drops):
        search_results.append({
            'title': search_result[0],
            'image': search_result[1],
            'price': search_result[2],
            'rating': search_result[3],
            'product_url': search_result[4],
            'price_drop': search_result[5],
        })'''
    return titles,images,prices

def parse_kara(url, sort=None):

    return []

def parse_konga(url, term):
    '''
    This function parses the page and returns list of torrents
    '''
    print(url)
    STORE = "konga"
    params = {"x-algolia-agent": "Algolia for vanilla JavaScript 3.30.0;react-instantsearch 5.3.2;JS Helper 2.26.1", "x-algolia-application-id": "B9ZCRRRVOM", "x-algolia-api-key": "cb605b0936b05ce1a62d96f53daa24f7"}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','accept': 'application/json','content-type': 'application/x-www-form-urlencoded','Origin': 'https://www.konga.com'}
    #formdata={"requests":[{"indexName":"catalog_store_konga_price_desc","params":"query=infinix%20hot%206&maxValuesPerFacet=50&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&facets=%5B%22special_price%22%2C%22attributes.brand%22%2C%22attributes.screen_size%22%2C%22attributes.ram_gb%22%2C%22attributes.sim%22%2C%22attributes.sim_slots%22%2C%22attributes.capacity%22%2C%22attributes.battery%22%2C%22attributes.connectivity%22%2C%22attributes.hard_drive%22%2C%22attributes.internal%22%2C%22attributes.tv_screen_size%22%2C%22attributes.operating_system%22%2C%22attributes.kids_shoes%22%2C%22attributes.heel_type%22%2C%22attributes.heel_height%22%2C%22attributes.leg_width%22%2C%22attributes.fastening%22%2C%22attributes.shirt_size%22%2C%22attributes.shoe_size%22%2C%22attributes.lingerie_size%22%2C%22attributes.pants_size%22%2C%22attributes.size%22%2C%22attributes.color%22%2C%22attributes.mainmaterial%22%2C%22konga_fulfilment_type%22%2C%22is_pay_on_delivery%22%2C%22is_free_shipping%22%2C%22pickup%22%2C%22categories.lvl0%22%5D&tagFilters=&ruleContexts=%5B%22%22%5D"}]}
    data = json.dumps({"requests" : [{"indexName":"catalog_store_konga_price_desc" ,"params":"query=" + re.sub(r"\s+", '%20', str(term))  }]})
    response = requests.post(url,headers=headers, params=params, data=data).json()    
    #soup = BeautifulSoup(data, 'lxml')
    print(response)
    #table_present = soup.find('div', {'class': 'ais-InstantSearch__root'})
    '''if table_present is None:
        return EMPTY_LIST
    titles = parse_titles(soup,STORE)
    images = parse_images(soup,STORE)
    prices = parse_prices(soup,STORE)
    #ratings = parse_ratings(soup,STORE)
    product_urls = parse_product_urls(soup,STORE)
    #price_drops = parse_price_drops(soup,STORE)
    search_results = []
    for search_result in zip(titles, images, prices, product_urls):
        search_results.append({
            'title': search_result[0],
            'image': search_result[1],
            'price': search_result[2],
            'url': search_result[3],
        })'''
    '''for search_result in zip(titles, images, prices, ratings, product_urls, price_drops):
        search_results.append({
            'title': search_result[0],
            'image': search_result[1],
            'price': search_result[2],
            'rating': search_result[3],
            'product_url': search_result[4],
            'price_drop': search_result[5],
        })'''
    return response

def parse_slot(url, sort=None):

    return []

def parse_titles(soup,STORE):
    switcher = {
        'jumia': parse_title_jumia,
        'konga': parse_title_konga,
        'kara': parse_title_kara,
        'slot': parse_title_slot
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Invalid Store")
    # Execute the function
    titles = func(soup)
    return titles


def parse_images(soup,STORE):
    switcher = {
        'jumia': parse_image_jumia,
        'konga': parse_image_konga,
        'kara': parse_image_kara,
        'slot': parse_image_slot
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Invalid Store")
    # Execute the function
    images = func(soup)
    return images

def parse_prices(soup,STORE):
    switcher = {
        'jumia': parse_price_jumia,
        'konga': parse_price_konga,
        'kara': parse_price_kara,
        'slot': parse_price_slot
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Invalid Store")
    # Execute the function
    images = func(soup)
    return images

def parse_ratings(soup,STORE):

    return

def parse_product_urls(soup,STORE):
    switcher = {
        'jumia': parse_url_jumia,
        'konga': parse_url_konga,
        'kara': parse_url_kara,
        'slot': parse_url_slot
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Invalid Store")
    # Execute the function
    urls = func(soup)
    return urls

def parse_price_drops(soup,STORE):

    return 

if __name__ == '__main__':
	app.debug = True
	app.run()
