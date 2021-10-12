import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')

data =  urllib.request.urlopen(url, context=ctx).read().decode()

js = json.loads(data)

sum = 0
for info in js['comments']:
    sum = sum +info['count']
print('Retrived:',len(data),'characters')
print('Count',len(js['comments']))
print('Sum:',sum)
