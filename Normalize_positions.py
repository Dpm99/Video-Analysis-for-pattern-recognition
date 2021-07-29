import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Ze\\Mao_esquerda_ze\\ze_esquerda.csv')

df = pd.DataFrame(df, columns = ['frames', 'x', 'y', 'dr'])
df.drop([0])

x = df['x'].tolist()
y = df['y'].tolist()

def norm_pos(lista_x, lista_y):

    lista_norm_x = []
    lista_norm_y = []
    media_x = np.mean(lista_x)
    media_y = np.mean(lista_y)
    desvio_padrao_x = np.std(lista_x)
    desvio_padrao_y = np.std(lista_y)

    for i in range(len(lista_x)):

        x_novo = (lista_x[i] - media_x) / desvio_padrao_x
        y_novo = (lista_y[i] - media_y) / desvio_padrao_y
        lista_norm_x.append(x_novo)
        lista_norm_y.append(y_novo)



    return(lista_norm_x, lista_norm_y)

normalizacao = norm_pos(x,y)

norm_x = normalizacao[0]
norm_y = normalizacao[1]

dados =  {'x': norm_x, 'y': norm_y}
base = pd.DataFrame(dados)

base.to_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Ze\\Mao_esquerda_ze\\ze_esquerda_posicoes_norm.txt')
