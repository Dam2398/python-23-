from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

num = soup.find_all('span', class_='comments') #TODA LA ETIQUETA
numeros = list()

for i in num:
    numeros.append(i.text)#EN UNA LISTA||obtener solo el texto de un html

#print(type(numeros)) saber que tipo es
#cnumeros = [int(x) for x in numeros]
cnumeros = list(map(int,numeros))#LISTA PERO ENTEROS

sum = 0
for i in cnumeros:
    sum = sum+i
print(sum)
