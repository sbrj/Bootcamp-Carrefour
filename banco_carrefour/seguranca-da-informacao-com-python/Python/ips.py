import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_network(ip)

print(endereco)