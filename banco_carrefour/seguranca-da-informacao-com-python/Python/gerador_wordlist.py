import itertools

string = 'acbdef'#input('Digite  a string a ser permutada: ')

resultado = itertools.permutations(string, len(string))

for letra in resultado:
    print("".join(letra))