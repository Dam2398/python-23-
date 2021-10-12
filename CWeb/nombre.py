from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

#http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
c = input('Enter count -')
p = input('Enter position -')
count= int(c)
position= int(p)
position=position-1


i=0

while i<count:
    x=0
    nombre = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        nombre.append(tag.text)
    if i==0:
        y = re.findall('y_(\S+)\.h',url)
        print("".join(y))
    print(nombre[position])
    for tag in tags:
        if x == position:
            url = tag.get('href',None)
        x+=1
    i+=1
