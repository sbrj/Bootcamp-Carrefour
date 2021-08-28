import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Cliente: Servidor? '

try:
    print(mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Retorno -", dados, '- Fim dados recebidos.')
except Exception as err:
    print(err)
finally:
    print('Cliente: Fechando a conexão com o servidor.')
    s.close()