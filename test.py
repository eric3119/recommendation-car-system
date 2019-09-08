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
    new_rec = True

    while new_rec:

        brands = data['brands']
        cosine_sim = []

        # ["Citroen", "Ford", 
        # "GM - Chevrolet", "Honda", 
        # "Hyundai", "Mitsubishi", 
        # "Peugeot", "Renault", 
        # "Toyota", "VW - VolksWagen"]

        print()
        
        pre_brand = -1
        pre_pot = -1
        pre_price = -1
        pre_year = ""

        for index, brand in enumerate(brands):
            print(f'[{index}] {brand}')

        while pre_brand < 0 or pre_brand >= len(brands):
            pre_brand = int(input('Marca: '))

        print()
        print('[_] 1.0')
        print('[_] 1.2')
        print('[_] 1.4')
        print('[_] 1.6')
        print('[_] 1.8')
        print('[_] 2.0')
        print('[_] 2.2')

        while pre_pot != 1.0 and pre_pot != 1.2 and pre_pot != 1.4 and\
            pre_pot != 1.6 and pre_pot != 1.8 and pre_pot != 2.0 and\
            pre_pot != 2.2:
            pre_pot = float(input('Cilindradas: '))

        print()
        print('Formato: DDDDD, Ex: 12250 || 25000')

        while pre_price <= 0:
            pre_price = float(input('Preço: '))

        print()
        print('Formato: DDDD, Ex: 2015')

        while len(pre_year) != 4:
            pre_year = input('Ano: ')
        
        pre_year = int(pre_year)

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
        print('Marca:', data['brands'][int(cif[3])])
        print('Ano:', int(cif[0]))
        print('Preço:', float(cif[2]))
        print('Cilindradas:', float(cif[1]))

        # Versão Eric ___________________
        # print()
        # print('Melhor Opção:')
        # print('Carro:', data['names'][result[0]])
        # print('Marca:', data['brands'][int(cif[1])])
        # print('Ano:', int(cif[0]))
        # print('Preço:', float(cif[2]))
        # print('Cilindradas:', float(cif[3]))

        print()
        answ = ""

        while answ != "S" and answ != "s" and answ != "N" and answ != "n":
            answ = input('Deseja realizar uma nova consulta? (S/n) ')
            if answ == "S" or answ == "s":
                new_rec = True
            else:
                new_rec = False


