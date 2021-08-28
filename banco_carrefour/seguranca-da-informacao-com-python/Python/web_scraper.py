from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())

temperatura = soup.find("span", id_='current-weather-temperature')

print(temperatura.string)
#print(temperatura.title.string)