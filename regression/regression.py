import pandas as pd
import json
from sklearn import linear_model

brands = [
    "Citroen",
    "Ford",
    "Chevrolet",
    "Honda",
    "Hyundai",
    "Mitsubishi",
    "Peugeot",
    "Renault",
    "Toyota",
    "VolksWagen"
]

features_name = [
    "potencia",
    "idade",
    "preco"
]

with open('freg.json') as car_info:
    data = json.load(car_info)


if __name__ == '__main__':
    new_rec = True

    while new_rec:

        pre_brand = -1
        pre_pot = -1
        pre_price = -1
        pre_year = -1

        for index, brand in enumerate(brands):
            print(f'[{index}] {brand}')

        print()

        while pre_brand < 0 or pre_brand >= len(brands):
            pre_brand = int(input('Marca: '))

        data_aux = data[brands[pre_brand]]
        df = pd.DataFrame(data_aux)
        df.columns = features_name
        # print(df)

        reg = linear_model.LinearRegression(fit_intercept=True, normalize=False)
        reg.fit(df[['potencia', 'idade']], df.preco)

        while pre_pot < 1:
            pre_pot = float(input('Cilindradas: '))

        while pre_year < 0:
            pre_year = int(input('Tempo do carro (anos): '))

        ### coeficiente de cada feature na equacao de regressao
        # print(reg.coef_)

        ### constante da equacao
        # print(reg.intercept_)

        resp = reg.predict([[pre_pot, pre_year]])

        ### Comparar todos
        # pred = reg.predict(df[['potencia', 'idade']])
        # compare = pd.DataFrame({'Real': df.preco, 'Estimado': pred.flatten()})
        # print(compare)

        print("\nO preço estimado para essa configuração é R$ %.2f\n" % (resp[0]))

        answ = ""
        while answ != "S" and answ != "s" and answ != "N" and answ != "n":
            answ = input('Deseja realizar uma nova consulta? (S/n) ')
            if answ == "S" or answ == "s":
                new_rec = True
            else:
                new_rec = False

