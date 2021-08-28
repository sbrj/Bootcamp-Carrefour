import os
import time
"""
Programa TCP básico, que recebe um IP para executar o ping
"""
print('#' * 50)
ip_host_verificar = input("digite o IP ou Host a ser verificado: ")
print('-' * 50)
os.system(f'ping -n 6 {ip_host_verificar}')
print('-' * 50)

