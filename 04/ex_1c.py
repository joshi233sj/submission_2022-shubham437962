from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

dataframe = pd.DataFrame({'name':[], 'Gen':[], 'Date':[]})

url = 'https://en.wikipedia.org/wiki/Queen_(band)'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    name = bs.find('h1').text
except:
    name = ''

try:
    gen = bs.find('th',string = 'Genres').next_sibling.text

except:
    gen = ''

try:
    date = bs.find('th',string = 'Years active').next_sibling.text

except:
    date = ''

extractedInfo = {'name':name, 'Gen':gen, 'Date':date}

dataframe = dataframe.append(extractedInfo, ignore_index = True)
print(dataframe)
