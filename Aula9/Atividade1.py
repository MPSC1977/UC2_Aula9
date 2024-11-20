import os

os.system('cls')

import pandas as pd

import numpy as np

idades = pd.Series([5, 10, 12, 35, 38])

conj_idades = np.array(idades)

variancia = np.var(conj_idades)
media = conj_idades.mean()
desvio_padrao = np.std(conj_idades)

print(f'Idades: {conj_idades}')

print(f'Média: {conj_idades.mean()}')

print(f'Variância: {np.var(conj_idades)}')

print(f'Desvio Padrão: {np.std(conj_idades):.2f}')

distancia_var_media = variancia / (media ** 2)
print(f'Distância: {distancia_var_media:.2f}')

coef_variacao = (desvio_padrao / media) * 100
print(f'Coef Variação: {coef_variacao:.2f}%')