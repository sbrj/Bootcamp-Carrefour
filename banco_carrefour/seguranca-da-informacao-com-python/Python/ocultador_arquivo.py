import ctypes

arquivo = 'arquivo_ocultado.txt'

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(arquivo, atributo_ocultar)

try:
    if retorno:
        print('Arquivo ocultado')

except Exception as err:
    print(err)
