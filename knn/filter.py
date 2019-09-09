import json
import re
import datetime
from unicodedata import normalize


def remover_acentos(s):
    return normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')


with open('../carros_pontos.json', 'r') as f:
    carrosJSON = json.load(f)

data = []
cilindradas = []
for carro in carrosJSON:

    marca = ''
    if carro['marca'] == 'VW - VolksWagen':
        marca = 'Volkswagen'
    elif carro['marca'] == 'GM - Chevrolet':
        marca = 'Chevrolet'
    else:
        marca = carro['marca']

    marca = remover_acentos(marca)
    nome = remover_acentos(carro['name'])

    cambio = 'Manual'
    if re.search("Aut", nome):
        cambio = 'Automatico'

    ano = carro['ano_modelo']
    date_format = '%Y'
    try:
        date_obj = datetime.datetime.strptime(ano, date_format)
    except ValueError:
        continue

    cilindrada = re.findall(r"[0-9]\.[0-9]", nome)
    if not cilindrada:
        continue
    if cilindrada[0] not in cilindradas:
        cilindradas.append(cilindrada[0])

    combustivel = 'Gasolina'
    if re.search(r"flex", nome, re.IGNORECASE):
        combustivel = 'Flex'

    data.append(
        {'nome': nome,
         'preco': carro['preco'],
         'marca': marca,
         'cambio': cambio,
         'combustivel': combustivel,
         'cilindrada': cilindrada[0],
         'ano': ano,
         })

with open('filtered.json', 'w') as f:
    json.dump(data, f, indent=1)
