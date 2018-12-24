import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

def getContentByURL(url):

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    return BeautifulSoup(html, "html.parser")


def getURLAndName(taglist, number):
    print(taglist)
    ii = 0
    for tag in taglist:
        if ii == number:
            return tag.get('href', None)
        ii = ii + 1



#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "http://py4e-data.dr-chuck.net/known_by_Munir.html"
loops = 7
hrefPosition = 18


for i in range(loops):

    soup = getContentByURL(url)

    print((i+1), 'loop name is', soup('a')[hrefPosition-1].contents[0])

    url = soup('a')[hrefPosition-1].get('href')

