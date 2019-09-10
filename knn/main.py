import os
import json
import pickle
from sklearn.neighbors import KNeighborsClassifier

if not os.path.isfile('filtered.json'):
    os.system("python filter.py")

with open('filtered.json', 'r') as f:
    jsonCarros = json.load(f)

features = []
labels = []
cambio = ['Manual', 'Automatico']
marcas = ['Citroen',
          'Ford',
          'Chevrolet',
          'Honda',
          'Hyundai',
          'Mitsubishi',
          'Peugeot',
          'Renault',
          'Toyota',
          'Volkswagen']

combustivel = ['Gasolina', 'Flex']


for carro in jsonCarros:
    features.append([carro['preco'],
                 carro['marca'],
                 carro['cambio'],
                 carro['combustivel'],
                 carro['cilindrada'],
                 carro['ano'],
                 ])
    labels.append(carro['nome'])


def user_input():
    print()
    for i in range(len(marcas)):
        print('[', i, '] ', marcas[i])
    pre_brand = int(input('Marca: '))

    print()
    for i in range(len(cambio)):
        print('[', i, '] ', cambio[i])
    pre_cambio = int(input('Cambio: '))

    print()
    for i in range(len(combustivel)):
        print('[', i, '] ', combustivel[i])
    pre_combust = int(input('Combustivel: '))

    print()
    pre_pot = float(input('Cilindradas [1.0 - 6.5]: '))

    print()
    pre_price = float(input('Preço: '))

    print()
    pre_year = int(input('Ano: '))
    return [pre_price, pre_brand, pre_cambio, pre_combust, pre_pot, pre_year]


def print_car(s):
    index = labels.index(s)
    print(marcas[features[index][1]], end=" ")
    print(s)
    print("R$", features[index][0])
    print(cambio[features[index][2]])
    print(combustivel[features[index][3]])
    print(features[index][4])
    print(features[index][5])
    print()


with open('cars_readable.txt', 'w') as f:
    for car in features:
        f.write("%s\n" % car)

with open('cars', 'wb') as f:
    pickle.dump(features, f)

with open('cars', 'rb') as f:
    features = pickle.load(f)

for i in range(len(features)):

    features[i][0] = features[i][0].replace('R$ ', '')
    features[i][0] = features[i][0].replace('.', '')
    features[i][0] = features[i][0].replace(',', '.')
    features[i][0] = float(features[i][0])  # preco

    features[i][1] = marcas.index(features[i][1])  # marca
    features[i][2] = cambio.index(features[i][2])  # cambio
    features[i][3] = combustivel.index(features[i][3])  # combustivel
    features[i][4] = float(features[i][4])  # cilindrada
    features[i][5] = int(features[i][5])  # ano

with open('cars_readable.txt', 'w') as f:
    for car in features:
        f.write("%s\n" % car)

to_predict = user_input()
#to_predict = [50000.0, 1, 1, 1, 1.5, 2014]
#to_predict = [46910.0, 0, 1, 1, 1.6, 2014]
# print("To predict: ", to_predict)

choose_brand = []
labels_brand = []

for i in range(len(features)):
    if features[i][1] == to_predict[1]:
        choose_brand.append(features[i])
        labels_brand.append(labels[i])

pesos = {
    'w': [1, 1, 10000, 1000, 1, 1]
} 

output = []
for k in range(1, 5):
    neigh = KNeighborsClassifier(n_neighbors=k, metric='wminkowski', metric_params = pesos)
    neigh.fit(choose_brand, labels_brand)
    res = neigh.predict([to_predict])

    if res not in output:
        output.append(res)

print("opções: ")
for x in output:
    print_car(x[0])
