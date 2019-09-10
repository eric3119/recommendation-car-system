from sklearn import tree
from sklearn.tree.export import export_text
import graphviz
import pickle
import os

data = []

# Run filter.py to generate data
if not os.path.isfile('cars'):
    os.system("python filter.py")

# Load data as a list from cars file
with open('cars', 'rb') as f:
    data = pickle.load(f)

# Split features and labels // Dont use brand
features = []
labels = []

for car in data:
    features.append(car[0:2])
    labels.append(car[3])


# Training Tree
def trainTree(feat, lab):

    clf = tree.DecisionTreeClassifier(criterion="entropy")
    clf = clf.fit(feat, lab)

    return clf


# Features columns names
feature_names = ["Price", "Year"]


# Save tree
def saveTree(filename, x):

    r = export_text(x, feature_names=feature_names)

    with open(filename, 'w') as f:
        f.write(r)


def getMenuOption(str, arr):
    print()
    for i, val in enumerate(arr):
        print(f'[{i}] {val}')

    option = int(input(f'{str}: '))
    print()
    return option


def printCar(arr, car_name):
    i = arr.index(car_name)
    value = data[i][0]
    year = data[i][1]
    brand = data[i][2]

    print(car_name[0])
    print("Marca: " + brand)
    print("Preco: " + str(value))
    print("Ano: " + str(year))
    print()


def filterBrand(brand):
    new_feat = []
    new_lab = []

    for x in range(len(data)):
        if data[x][2] == brand:
            new_feat.append(features[x])
            new_lab.append(labels[x])

    return new_feat, new_lab


marcas = [
    "Citroen",
    "Ford",
    "Chevrolet",
    "Honda",
    "Hyundai",
    "Peugeot",
    "Renault",
    "Toyota",
    "Volkswagen"
]

while True:
    print("Tem preferencia por alguma marca?")
    print("[0] - Nao\n[1] - Sim")
    flag_filter = int(input("Resp: "))

    n_features = features
    n_labels = labels

    if flag_filter == 1:
        brand = marcas[getMenuOption("Choose brand: ", marcas)]
        n_features, n_labels = filterBrand(brand)
    else:
        brand = "Todas"

    print("Marca escolhida: " + brand)

    _tree = trainTree(n_features, n_labels)
    saveTree('last_tree.txt', _tree)

    to_predict = [0, 0]
    to_predict[0] = int(input("Valor desejado: "))
    to_predict[1] = int(input("Ano desejado: "))

    prediction_car_name = _tree.predict([to_predict])

    print("Carro selecionado: " + str(prediction_car_name[0]))
    print()