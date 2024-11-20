import os

os.system('cls')

import pandas as pd

import numpy as np

dados = pd.Series([2, 4, 6, 8, 10])

conjunto_dados = np.array(dados)
media = conjunto_dados.mean()
variancia = np.var(conjunto_dados)
desvio_padrao = np.std(conjunto_dados)

variancia_amostral = np.var(conjunto_dados, ddof=1)
desvio_padrao_amostral = np.std(conjunto_dados, ddof=1)

print(f'Conjunto de dados: {conjunto_dados}')

print(f'Média: {conjunto_dados.mean()}')

print(f'Variância: {np.var(conjunto_dados)}')

print(f'Desvio Padrão: {np.std(conjunto_dados):.2f}')

distancia_var_media = variancia / (media ** 2)
print(f'Distância: {distancia_var_media:.2f}')

coef_variacao = (desvio_padrao / media) * 100
print(f'Coef Variação: {coef_variacao:.2f}%')

print(f'Variância Amostral {variancia_amostral:.2f}')
print(f'Desvio Padrão Amostral Amostral {desvio_padrao_amostral:.2f}')