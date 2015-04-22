# XML Parser
import requests
from bs4 import BeautifulSoup

URL = 'http://www.elections.ny.gov/CountyBoards.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content)

# Get the county URLS from the <area> tag
counties = soup.select("area")
county_urls = [u.get('href') for u in counties]

# skip the dummy URL
county_urls = county_urls[1:]

county_urls = list(set(county_urls))

# Store results
data = []

for URL in county_urls:
  print "Fetching %s" % URL
  page = requests.get(URL)
  soup = BeautifulSoup(page.content)
  lines = [s for s in soup.select("th") [0].strings]
  data.append(lines)

output = open("boards.txt", "w")
for row in data:
  output.write("\t".join(row) + "\n")

count = 0

for line in BOARDS_FILE:
  count = count + 1
print "Line count: ", count

output.close()