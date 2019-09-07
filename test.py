import pandas as pd
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity

data = []

with open('car_info.json') as car_info:
    data = json.load(car_info)

def filter(arr):
    return arr[1]

table = pd.read_json('nfil.json').to_numpy()

if __name__ == '__main__':

    cosine_sim = []

    # ["Citroen", "Ford", 
    # "GM - Chevrolet", "Honda", 
    # "Hyundai", "Mitsubishi", 
    # "Peugeot", "Renault", 
    # "Toyota", "VW - VolksWagen"]

    print()
    print('[0] Citroen')
    print('[1] Ford')
    print('[2] Chevrolet')
    print('[3] Honda')
    print('[4] Hyundai')
    print('[5] Mitsubishi')
    print('[6] Peugeot')
    print('[7] Renault')
    print('[8] Toyota')
    print('[9] Volkswagen')
    pre_brand = int(input('Marca: '))

    print()
    print('[_] 1.0')
    print('[_] 1.2')
    print('[_] 1.4')
    print('[_] 1.6')
    print('[_] 1.8')
    print('[_] 2.0')
    print('[_] 2.2')
    pre_pot = float(input('Cilindradas: '))

    print()
    print('Formato: DD.DDD, Ex: 12.250')
    pre_price = float(input('Preço: '))

    print()
    print('Formato: DDDD, Ex: 2015')
    pre_year = int(input('Ano: '))

    predict = np.array([pre_brand, pre_pot, pre_price, pre_year])

    for index, row in enumerate(table):
        a = predict.reshape(1, 4)
        b = row.reshape(1, 4)
        cos_sim = cosine_similarity(a, b)
        res = [index, cos_sim[0][0]]
        cosine_sim.append(res)

    result = max(cosine_sim, key=filter)

    cif = table[result[0]]

    print()
    print('Melhor Opção:')
    print('Carro:', data['names'][result[0]])
    print('Marca:', data['brands'][int(cif[0])])
    print('Ano:', int(cif[3]))
    print('Preço:', float(cif[2]))
    print('Cilindradas:', float(cif[1]))

