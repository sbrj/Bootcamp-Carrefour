import socket 
import sys

def main():
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except Exception as err:
        print('A Conexão falhou! \nErro: ', err)
        sys.exit()

    print("Socket criado com sucesso")

    hostAlvo = input("Digite o Host ou IP: ")
    portaAlvo = input("Digite a porta: ")

    try:
        soc.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no Host", hostAlvo, "e na porta", portaAlvo)
        soc.shutdown(2)
    except Exception as err:
        print("A conexão falhou com o Host:", hostAlvo, "e porta", portaAlvo)
        print(f"Erro: {err}")
        sys.exit()


if __name__ == "__main__":
    main()