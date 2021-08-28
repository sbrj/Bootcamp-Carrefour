import hashlib

ar1 = 'a.txt'
ar2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open( ar1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(ar2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'o {ar1} é diferente do {ar2}')
    print(f'Hash 1 - {hash1.hexdigest()}')
    print(f'Hash 2 - {hash2.hexdigest()}')
else:
    print('São iguais')
    print(f'Hash 1 - {hash1.hexdigest()}')
    print(f'Hash 2 - {hash2.hexdigest()}')


