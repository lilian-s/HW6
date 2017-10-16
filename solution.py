# Name: Lilian Sheu
# Discussion: Thursday 3-4pm

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# sample data url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# real data url: http://py4e-data.dr-chuck.net/known_by_Aimie.html
url = input('Enter URL: ')

count = int(input('Enter count: '))
pos = int(input('Enter position: '))

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser


# Retrieve all of the anchor tags
last_output = ''
for i in range(count):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	last_output = tags[pos-1].contents[0]
	url = tags[pos-1].get('href', None)
    #print(tags[i].attrs)
print(last_output)