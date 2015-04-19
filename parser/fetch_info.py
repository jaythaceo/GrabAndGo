# XML Parser
import urllib
from bs4 import BeautifulSoup

URL = 'http://www.cbssports.com/mlb/stats/playersort/mlb/year-2015-season-regularseason-category-batting-qualifying-1'

html = urllib.urlopen(URL).read()
soup = BeautifulSoup(html)
tags = soup('tr')

for tag in tags:
  tag.get('id', None)