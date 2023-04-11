from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
Summary = 0
Count = 0
Numbers = []
# Retrieve all of the anchor tags
comments = soup('span')
for comment in comments:
    # print(comment.contents[0])
    Count = Count + 1
    Summary = Summary + int(comment.contents[0])
print(Count)
print(Summary)
