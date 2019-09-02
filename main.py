from sklearn import tree

def realMoneyMask(my_value):
    val = float(my_value)
    a = '{:,.2f}'.format(val)
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def printCar(arr, car_name):
    i = arr.index(car_name)
    info = features[i]
    value = realMoneyMask(original_prices[i])
    brand = brands[info[1]]
    fuel_t = fuel[info[2]]
    transmission_t = transmissions[info[3]]
    cylinder_t = cylinder_cap[info[4]]
    doors_str = doors[info[5]]

    print(f'Modelo: {brand} {car_name[0]}')
    print(f'Valor: R$ {value}')
    print(f'Marca: {brand}')
    print(f'Tipo de Combustível: {fuel_t}')
    print(f'Transmissão: {transmission_t}')
    print(f'Cilindradas: {cylinder_t}')
    print(f'Portas: {doors_str}')

def getMenuOption(str, arr):
    print()
    for i, val in enumerate(arr):
        print(f'[{i}] {val}')
        
    option = int(input(f'{str}: '))
    return option

"""
- Preco
- Marcas
    0 Citroen
    1 Ford
    2 Chevrolet
    3 Honda
    4 Hyundai
    5 Peugeot
    6 Renault
    7 Toyota
    8 Volkswagen
- Gasolina
    0 Gasolina
    1 Flex
- Cambio
    0 Manual
    1 Automatico
- Cilindrada
    0 1.4
    1 1.6
    2 1.8
    3 2.0
- Portas
    0 2 Portas
    1 4 Portas
"""

original_prices = [
    46910,
    38301,
    17343,
    33006,
    102839,
    135981,
    14857,
    68958,
    75435,
    58161,
    37282,
    68388,
    21081,
    43646,
    92344,
    60589,
    39022,
    17321,
    58568,
    63811,
    43155,
    29383,
    81599,
    86368,
    26646,
    136094,
    17727,
    21125,
    122549,
    76600
]

prices_categ = [
    "Entre 10.000 e 20.000", # 0, [10000, 20000)
    "Entre 20.000 e 30.000", # 1, [20000, 30000)
    "Entre 30.000 e 40.000", # 2, [30000, 40000)
    "Entre 40.000 e 50.000", # 3, [40000, 50000)
    "Entre 50.000 e 60.000", # 4, [50000, 60000)
    "Entre 60.000 e 70.000", # 5, [60000, 70000)
    "Entre 70.000 e 80.000", # 6, [70000, 80000)
    "Entre 80.000 e 90.000", # 7, [80000, 90000)
    "Acima de 90.000"        # 8, > 90000
]

brands = [
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

fuel = ["Gasolina", "Flex"]
transmissions = ["Manual", "Automático"]
cylinder_cap = ["1.4", "1.6", "1.8", "2.0"] 
doors = ["2 Portas", "4 Portas"]

features = [
    [3, 0, 1, 1, 1, 1],
    [2, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 3, 1],
    [2, 0, 0, 1, 3, 1],
    [8, 0, 0, 1, 1, 1],
    [8, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [5, 1, 1, 1, 1, 1],
    [6, 2, 1, 1, 2, 1],
    [4, 2, 1, 1, 0, 1],
    [2, 2, 1, 1, 1, 1],
    [5, 2, 1, 1, 2, 1],
    [1, 2, 0, 0, 3, 1],
    [3, 3, 1, 1, 0, 1],
    [8, 3, 1, 1, 2, 1],
    [5, 4, 1, 1, 1, 1],
    [2, 4, 0, 1, 3, 1],
    [0, 5, 1, 1, 1, 1],
    [4, 5, 1, 1, 1, 1],
    [5, 5, 0, 1, 1, 1],
    [3, 5, 0, 0, 3, 0],
    [1, 5, 0, 1, 3, 1],
    [7, 5, 1, 1, 1, 1],
    [7, 5, 0, 1, 1, 1],
    [1, 5, 0, 1, 3, 1],
    [8, 5, 0, 1, 1, 0],
    [0, 6, 1, 1, 1, 1],
    [1, 6, 1, 1, 1, 1],
    [8, 7, 0, 1, 2, 1],
    [6, 8, 0, 0, 0, 1]
]

labels = [
    "AIRCROSS", "C4", "C5", "C8", "DS4", "DS5", "Xsara", "Focus", "CRUZE", "PRISMA", "SONIC", "SPIN", 
    "Zafira", "Fit", "HR-V", "i30", "i30cw", "206", "208", "3008", "307", "407", "408", "508", "807", 
    "RCZ", "LOGAN", "SANDERO", "PRIUS", "JETTA"
]

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(features, labels)

if __name__ == '__main__':
    to_predict = [0, 0, 0, 0, 0, 0]
    to_predict[0] = int(getMenuOption("Valor", prices_categ))
    to_predict[1] = int(getMenuOption("Marca", brands))
    to_predict[2] = int(getMenuOption("Tipo de Combustível", fuel))
    to_predict[3] = int(getMenuOption("Transmissão", transmissions))
    to_predict[4] = int(getMenuOption("Cilindradas", cylinder_cap))
    to_predict[5] = int(getMenuOption("Portas", doors))

    prediction = clf.predict([to_predict])

    print()
    printCar(labels, prediction)