from bs4 import BeautifulSoup
import requests
import pandas as pd
#Programa para sacar precios de amazon
url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser' )  #tranformando a formato BeautifulSoup|| Identificar los diferentes elementos de html

#Equipos
eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()
#pos = list()

count = 0
for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count +=1

#Posiciones
pos = soup.find_all('td', class_='destacado')
posicion = list()

count = 0
for i in pos:
    if count < 20:
        posicion.append(i.text)
    else:
        break
    count +=1

#Frame||pandas
tabla = pd.DataFrame({'Nombre':equipos, 'Puntos':posicion}, index= list(range(1,21)))
print(tabla)
