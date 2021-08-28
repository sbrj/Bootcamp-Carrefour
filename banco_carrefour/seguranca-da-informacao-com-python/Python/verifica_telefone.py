import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato +5521992014952: ')

numero_telefone = phonenumbers.parse(phone)

print(geocoder.description_for_number(numero_telefone, 'pt'))
