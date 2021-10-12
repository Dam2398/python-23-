import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
#address='South Federal University'

parms = dict()#crea una variale tipo diccionario
parms['address'] = address
parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms) #codificamos lo paramatros{'address': 'South Federal University', 'key': 42} para incluirlos en la liga

print('Retrieving',url)
uh = urllib.request.urlopen(url,context=ctx)
data = uh.read().decode()
print('Retrieving',len(data),'characters')

js = json.loads(data)

print('Place id',js['results'][0]['place_id'])
