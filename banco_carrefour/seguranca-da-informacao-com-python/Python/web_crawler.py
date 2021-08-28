import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup  = BeautifulSoup(source_code, 'html.parser')

    for cada_texto in soup.findAll('div', {'class': 'entry-content'}):
        content = cada_texto.text

        palavras = content.lower().split()

        for palavra in palavras:
            wordlist.append(palavra)
        
        limpa_lista(palavras)

def limpa_lista(l_palavras):
    lista_limpa = []
    for l_palavra in l_palavras:
        simbolos = '!@#$%&*()_-+={[]}|\;:"<>?/., '

        for subs in range(0, len(simbolos)):
            l_palavra = l_palavra.replace(simbolos[subs], '')

        if len(l_palavra) > 0:
            lista_limpa.append(l_palavra)
    
    criar_dicionario(lista_limpa)

def criar_dicionario(d_lista_limpa):
    contador_palavra = {}

    for d_palavra in d_lista_limpa:
        if d_palavra in contador_palavra:
            contador_palavra[d_palavra] += 1
        else: 
            contador_palavra[d_palavra] = 1
    
    for chave, valor in sorted(contador_palavra.items(), key = operator.itemgetter(1)):
        print(chave,":" ,valor)

    c = Counter(contador_palavra)
    
    principais = c.most_common(10)

    print(principais)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
