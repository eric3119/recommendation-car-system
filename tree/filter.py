import json
import re
import pickle

with open("./carros_pontos.json") as f:
    data = json.load(f)

f.close()

result = []

for car in data:
    price = int(re.sub("[.]*", '', car['preco'][3:-3]))
    year = (int(car['ano_modelo']))
    brand = car['marca']
    name = car['name'] + " price " + str(price) + " year " + str(year)

    if 1950 < year < 2020:
        if brand == 'VW - VolksWagen':
            brand = 'Volkswagen'
        elif brand == 'GM - Chevrolet':
            brand = 'Chevrolet'
        elif brand == 'Citroën':
            brand = 'Citroen'

        result.append([price, year, brand, name])


print(len(result))

with open('tree/cars_readable.txt', 'w') as f:
    for car in result:
        f.write("%s\n" % car)

with open('tree/cars', 'wb') as f:
    pickle.dump(result, f)