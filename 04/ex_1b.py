from urllib import request
from bs4 import BeautifulSoup as BS

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('ul')[4].find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]

for link in links:
    print(link)
