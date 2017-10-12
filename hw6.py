# Name: Lilian Sheu
# Discussion: Thursday 3-4pm

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# sample data url: http://py4e-data.dr-chuck.net/comments_42.html
# real data url: http://py4e-data.dr-chuck.net/comments_31741.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum_url = 0
for tag in tags:
    sum_url += int(tag.contents[0])
print ('Sum', sum_url)