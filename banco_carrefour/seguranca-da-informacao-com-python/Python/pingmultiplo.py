import os
from time import sleep


with open('hosts.txt') as arquivo:
    dump = arquivo.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP: ', ip)
        try:
            os.system(f'Ping -n 2 {ip}')
        except Exception as err:
            print(err)

        sleep(3)        
        print('---------------------------\n')