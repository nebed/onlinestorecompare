
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
    Returns list of titles of products from store
    '''
    titles = soup.find_all("span", class_="name")
    titles[:] = [title.get_text() for title in titles]

    return titles

def parse_image_konga(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("div", class_="af885_1iPzH")
    titles[:] = [title.h3.get_text() for title in titles]

    return titles

def parse_image_kara(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("h2", class_="product-name")
    titles[:] = [title.a.get('title') for title in titles]

    return titles

def parse_image_slot(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all(class_="product-content")
    titles[:] = [title.h2.a.get_text() for title in titles]

    return titles