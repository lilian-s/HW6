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
html = urllib.request.urlopen(url, context=ctx).read()

count = input('Enter count: ')
pos = input('Enter position: ')

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	print(tag.contents[0])
    #print(tag.get('href', None))