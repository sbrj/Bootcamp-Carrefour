from threading import Thread
from time import sleep

def carro(piloto, velocidade):
    trajeto = 0
    while trajeto <= 10:
        trajeto += velocidade
        sleep(.5)
        print(f'\nPiloto: {piloto}\nTrajeto percorrido: {trajeto}')

t_carro1 = Thread(target=carro, args=['Mau', 1])
t_carro2 = Thread(target=carro, args=['Bru', 2])

t_carro1.start()
t_carro2.start()