import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = input('Enter - ')

xml = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved', len(xml), 'characters')
#print(xml.decode())#Obetenemos el xml con decode

tree = ET.fromstring(xml)
#print(tree)

resul = tree.findall('.//count')
print(len(resul))

for i in resul:
    print(i.text)
num=list()
sum=0
for x in resul:
    num = int(x.text)
    sum = sum+num

print(sum)
