################################################################################
# Parsing HTML using Beautiful Soup
################################################################################
# This pogram abuses the style of text to extract either red or green parts.

from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd


url = 'https://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')



bs_name_list = bs.find_all('span', {'class':'excitingNote'})
for name in bs_name_list:
    print(" Bold Text is: " + name.get_text())

name_list = [name.get_text() for name in bs_name_list]
DF = pd.DataFrame(name_list)

print("DF :" + DF)



Title = bs.find('tr', {'id':'gift5'}).td.text
print("Title is: " + Title)



footer= bs.find('div', {'id':'footer'}).get_text()
print("Footer is: " + footer)
