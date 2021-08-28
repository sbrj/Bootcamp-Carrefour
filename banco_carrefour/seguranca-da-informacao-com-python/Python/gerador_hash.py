import hashlib

#string_hash = input('Digite o texto do hash a ser gerado: ')
string_hash = "legal legal"
imprime_menu = print('''
### MENU - ESCOLHA O TIPO DE HASH ###

1) MD5
2) SHA1
3) SHA256
4) SHA512
            ''')
            
def f_menu():
    menu = int(input('Digite o número do hash a ser gerado: '))
    if menu == 1:
        resultado = hashlib.md5(string_hash.encode('utf-8'))
        print('A hash MD5 da string: ',string_hash, 'é', resultado.hexdigest())    
    elif menu == 2:
        resultado = hashlib.sha1(string_hash.encode('utf-8'))
        print('A hash SHA1 da string: ',string_hash, 'é', resultado.hexdigest())    
    elif menu == 3:
        resultado = hashlib.sha256(string_hash.encode('utf-8'))
        print('A hash SHA256 da string: ',string_hash, 'é', resultado.hexdigest())    
    elif menu == 4:
        resultado = hashlib.sha512(string_hash.encode('utf-8'))
        print('A hash SHA512 da string: ',string_hash, 'é', resultado.hexdigest())    
    else:
        print('Algo de errado, não deu certo!')

if __name__ == '__main__':
    while True:
        f_menu()
        continuar = int(input("Continuar? Digite 1 para continuar."))
        if continuar != 1:
            break
    