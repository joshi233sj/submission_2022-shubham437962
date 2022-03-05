import sys
from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')


dob = bs.find('span', {'class':'bday'}).getText()
print("Date of Birth is: " + dob)


occ = bs.find_all('div',{'class':'hlist hlist-separated'})
print()
for text in occ:
    print("occupations are: " + text.get_text(separator=","))


ref =  bs.find_all('div',{'class':'mw-references-wrap mw-references-columns'})

for text in ref:
    print("References are: " + text.get_text())






