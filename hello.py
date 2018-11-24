import os

import requests
import re
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request
from store_functions import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

JUMIA_URL = os.getenv('JUMIA_URL', 'https://www.jumia.com.ng/?q=')
KONGA_URL = os.getenv('KONGA_URL', 'https://www.konga.com/search?search=')
KARA_URL = os.getenv('KARA_URL', 'http://www.kara.com.ng/catalogsearch/result?q=')
SLOT_URL = os.getenv('SLOT_URL', 'https://slot.ng/?post_type=product&s=')

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

    jumiaurl = JUMIA_URL + str(term)
    kongaurl = KONGA_URL + str(term)
    karaurl = KARA_URL + str(term)
    sloturl = SLOT_URL + str(term)
    jumiaresult=parse_jumia(jumiaurl)
    kararesult=parse_kara(karaurl)
    kongaresult=parse_konga(kongaurl)
    slotresult=parse_slot(sloturl)

    return jsonify(results), 200

def parse_jumia(url, sort=None):
    '''
    This function parses the page and returns list of torrents
    '''
    STORE = "jumia"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')
    table_present = soup.find('section', {'class': 'products osh_gallery-no_gutter'})
    if table_present is None:
        return EMPTY_LIST
    titles = parse_titles(soup,STORE)
    images = parse_images(soup,STORE)
    prices = parse_prices(soup,STORE)
    ratings = parse_ratings(soup,STORE)
    product_urls = parse_product_urls(soup,STORE)
    price_drops = parse_price_drops(soup,STORE)
    search_results = []
    for search_result in zip(titles, images, prices, ratings, product_urls, price_drops):
        search_results.append({
            'title': search_result[0],
            'image': search_result[1],
            'price': search_result[2],
            'rating': search_result[3],
            'product_url': search_result[4],
            'price_drop': search_result[5],
        })

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

    return

def parse_price_drops(soup,STORE):

    return 

if __name__ == '__main__':
	app.debug = True
	app.run()
