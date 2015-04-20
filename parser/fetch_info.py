# XML Parser
import urllib
from bs4 import BeautifulSoup

"""

"""


URL = 'http://espn.go.com/mlb/stats/batting/_/year/2015/seasontype/2'
html = urllib.urlopen(URL).read()
soup = BeautifulSoup(html)
tags = soup('oddrow')

"""
for tag in tags:    # Players IDs
  tag.get('id')
"""

for link in tags:
  print link.get('t')