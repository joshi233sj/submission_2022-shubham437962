from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Download and import to Beautiful Soup already known page:
url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

#### Exercise 2 - Flags (Medium) ####

images = bs.find_all('img', {'src':re.compile('\/\/upload\.wikimedia\.org\/wikipedia\/[a-z]+\/[a-z]+\/[0-9a-z]+\/[0-9a-z]+\/Flag_of_[a-z_A-Z]+\.svg\/[0-9a-z-A-Z_]+\.svg\.png')})

for image in images:
    print(image['src'])
