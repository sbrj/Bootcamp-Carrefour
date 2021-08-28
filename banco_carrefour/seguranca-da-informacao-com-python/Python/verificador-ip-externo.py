import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
cep = dados['postal']
loc = dados['loc']

print('Detalhes do IP externo\n')
print(f'-IP: {ip}\n-Provedor: {org}\n-Cidade: {cid}\n-País: {pais}\n-Região: {regiao}\n-CEP: {cep}\n-Localização: {loc}')