
from re import sub

def parse_title_jumia(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("span", class_="name")
    titles[:] = [title.get_text() for title in titles]

    return titles

def parse_title_konga(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("div", class_="af885_1iPzH")
    titles[:] = [title.h3.get_text() for title in titles]

    return titles

def parse_title_kara(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("h2", class_="product-name")
    titles[:] = [title.a.get('title') for title in titles]

    return titles

def parse_title_slot(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all(class_="product-content")
    titles[:] = [title.h2.a.get_text() for title in titles]

    return titles

def parse_image_jumia(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all("div", class_="image-wrapper")
    images[:] = [image.img.get('data-src') for image in images]

    return images

def parse_image_konga(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all("img", class_="_7e903_3FsI6")
    images[:] = [image.a.picture.img.get('src') for image in images]

    return images

def parse_image_kara(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all("div", class_="prolabel-wrapper")
    images[:] = [image.a.img.get('src') for image in images]

    return images

def parse_image_slot(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all(class_="mf-product-thumbnail")
    images[:] = [image.img.get('src') for image in images]

    return images

def parse_price_jumia(soup):
    '''
    Returns list of images of products from store
    '''
    prices = soup.find_all("span", class_="price-box ri")
    print(prices)
    prices[:] = [price.span.find("span", dir="ltr").get('data-price') for price in prices]

    return prices

def parse_price_konga(soup):
    '''
    Returns list of prices of products from store
    '''
    prices = soup.find_all("span", class_="d7c0f_sJAqi")
    prices[:] = [price.get_text() for price in prices]

    return prices

def parse_price_kara(soup):
    '''
    Returns list of prices of products from store
    '''
    prices = soup.find_all("span", class_="price")
    prices[:] = [ sub(r'[^\d.]', '', price.get_text())  for price in prices]

    return prices

def parse_price_slot(soup):
    '''
    Returns list of prices of products from store
    '''
    prices = soup.find_all('span', class_="woocommerce-Price-amount amount")
    prices[:] = [price.get_text() for price in prices]

    return prices
