import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

def getContentByURL(url):

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    return BeautifulSoup(html, "html.parser")


url = "http://py4e-data.dr-chuck.net/comments_166088.xml"

soup = getContentByURL(url)

totalSum = 0

for tmpCount in soup('count'):
    totalSum = totalSum + int(tmpCount.contents[0])

print(totalSum)