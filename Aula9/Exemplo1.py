import os

os.system('cls')

dados = {1, 2, 3, 4, 5}

media = sum(dados) / len(dados)
print(f'Média: {media}')

diferencas = [x - media for x in dados]
print(f'Diferença: {diferencas}')

quadrados_diferencas = [x**2 for x in diferencas]
print(f'Quadrados {quadrados_diferencas}')

media_quadrados_diferencas = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f'Variância: {media_quadrados_diferencas}')

desvio_padrao = media_quadrados_diferencas ** 0.5
print(f'Desvio Padrão: {desvio_padrao:.2f}')

distancia_var_media = media_quadrados_diferencas / (media ** 2)
print(f'Distância: {distancia_var_media:.2f}')

coef_variacao = (desvio_padrao / media) * 100
print(f'Coef Variação: {coef_variacao:.2f}%')