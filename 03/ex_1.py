from urllib import request
from bs4 import BeautifulSoup as BS
import pandas as pd

#  import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')



selected_tags = bs.find_all(lambda tag: ("Anna Pavlovna" in tag.get_text()))

print(len(selected_tags))

one_attribute_tag = bs.find_all(lambda tag: (len(tag.attrs) == 1))


for tags in one_attribute_tag:
    print(tags.get_text(separator="\n"))

print(len(one_attribute_tag))
