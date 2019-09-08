###
# Faz regressao do preco com base no tempo do carro, e na potencia
# ## criei esse dataset provisorio
# ## observei que colocando mais de uma marca a regressao nao fica precisa
#

import pandas as pd
from sklearn import linear_model

features_prov = [
    "marca1",
    "marca2",
    "potencia",
    "idade",
    "preco"
]

# marca1 -> barata
# marca2 -> cara
data_prov = [
    [1, 0, 2.0, 4, 70000],
    [1, 0, 1.6, 2, 65000],
    [1, 0, 1.0, 2, 35000],
    [1, 0, 2.2, 1, 110000],
    [1, 0, 2.0, 5, 65000]#, marca2 inicio
#    [0, 1, 2.0, 4, 160000],
#    [0, 1, 1.6, 2, 145000],
#    [0, 1, 1.0, 2, 105000],
#    [0, 1, 2.2, 1, 250000],
#    [0, 1, 2.0, 5, 150000]
]

df = pd.DataFrame(data_prov)
df.columns = features_prov
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['marca1', 'marca2', 'potencia', 'idade']], df.preco)

# coeficiente de cada feature na equacao de regressao
print(reg.coef_)

# constante da equacao
print(reg.intercept_)

print(reg.predict([[1, 0, 1.0, 2]]))