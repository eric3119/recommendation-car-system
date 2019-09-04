from sklearn import tree
import pickle
import os

data = []

# Run filter.py to generate data
if not os.path.isfile('cars'):
    os.system("python filter.py")

# Load data as a list from cars file
with open('cars', 'rb') as f:
    data = pickle.load(f)


features = []
labels = []

# Split features and labels
for car in data:
    features.append(car[0:2])
    labels.append(car[3])

# Features columns names
features_names = ["Price", "Year"]

# Training Tree
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(features, labels)

# Print tree

# tree.plot_tree(clf)
# r = export_text(clf, feature_names=features_names)
# print(r)

def printCar(arr, car_name):
    i = arr.index(car_name)
    value = data[i][0]
    year = data[i][1]
    brand = data[i][2]

    print(car_name[0])
    print("Marca: " + brand)
    print("Preco: " + str(value))
    print("Ano: " + str(year))



while True:
    to_predict = [0, 0]
    to_predict[0] = int(input("Valor: "))
    to_predict[1] = int(input("Ano: "))

    prediction = clf.predict([to_predict])

    print()
    printCar(labels, prediction)