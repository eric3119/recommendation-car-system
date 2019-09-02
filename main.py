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
    value = realMoneyMask(info[0])
    brand = brands[info[1]]
    fuel_t = fuel[info[2]]
    transmission_t = transmissions[info[3]]
    cylinder_t = cylinder_cap[info[4]]
    doors = info[5]

    print(f'Modelo: {brand} {car_name[0]}')
    print(f'Valor: R$ {value}')
    print(f'Marca: {brand}')
    print(f'Tipo de Combustível: {fuel_t}')
    print(f'Transmissão: {transmission_t}')
    print(f'Cilindradas: {cylinder_t}')
    print(f'Portas: {doors} Portas')

def getMenuOption(str, arr):
    print()
    for i, val in enumerate(arr):
        print(f'[{i}] {val}')
        
    option = int(input(f'{str}: '))
    return option

"""
- Preco
- Marcas
    1 Citroen
    2 Ford
    3 Chevrolet
    4 Honda
    5 Hyundai
    6 Peugeot
    7 Renault
    8 Toyota
    9 Volkswagen
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
"""

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
    [46910,  1, 1, 1, 1, 4],
    [38301,  1, 1, 0, 1, 4],
    [17343,  1, 0, 0, 3, 4],
    [33006,  1, 0, 1, 3, 4],
    [102839, 1, 0, 1, 1, 4],
    [135981, 1, 0, 1, 1, 4],
    [14857,  1, 0, 1, 1, 4],
    [68958,  2, 1, 1, 1, 4],
    [75435,  3, 1, 1, 2, 4],
    [58161,  3, 1, 1, 0, 4],
    [37282,  3, 1, 1, 1, 4],
    [68388,  3, 1, 1, 2, 4],
    [21081,  3, 0, 0, 3, 4],
    [43646,  4, 1, 1, 0, 4],
    [92344,  4, 1, 1, 2, 4],
    [60589,  5, 1, 1, 1, 4],
    [39022,  5, 0, 1, 3, 4],
    [17321,  6, 1, 1, 1, 4],
    [58568,  6, 1, 1, 1, 4],
    [63811,  6, 0, 1, 1, 4],
    [43155,  6, 0, 0, 3, 2],
    [29383,  6, 0, 1, 3, 4],
    [81599,  6, 1, 1, 1, 4],
    [86368,  6, 0, 1, 1, 4],
    [26646,  6, 0, 1, 3, 4],
    [136094, 6, 0, 1, 1, 2],
    [17727,  7, 1, 1, 1, 4],
    [21125,  7, 1, 1, 1, 4],
    [122549, 8, 0, 1, 2, 4],
    [76600,  9, 0, 0, 0, 4]
]

labels = [
    "AIRCROSS", "C4", "C5", "C8", "DS4", "DS5", "Xsara", "Focus", "CRUZE", "PRISMA", "SONIC", "SPIN", 
    "Zafira", "Fit", "HR-V", "i30", "i30cw", "206", "208", "3008", "307", "407", "408", "508", "807", 
    "RCZ", "LOGAN", "SANDERO", "PRIUS", "JETTA"
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

if __name__ == '__main__':
    to_predict = [0, 0, 0, 0, 0, 0]
    to_predict[0] = int(input('Valor (Aproximado): '))
    to_predict[1] = int(getMenuOption("Marca", brands))
    to_predict[2] = int(getMenuOption("Tipo de Combustível", fuel))
    to_predict[3] = int(getMenuOption("Transmissão", transmissions))
    to_predict[4] = int(getMenuOption("Cilindradas", cylinder_cap))
    to_predict[5] = int(getMenuOption("Portas", doors))

    prediction = clf.predict([to_predict])

    print()
    printCar(labels, prediction)