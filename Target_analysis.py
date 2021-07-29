import matplotlib.pyplot as plt
import numpy as np
import math
import PIL
import glob
import matplotlib.pyplot as plt
from skimage import data, io, filters
from os import listdir
from os.path import isfile, join
import csv
import colorsys
from pathlib import Path
from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.animation as animation
import cv2


Area_ref = []
raio_ref = []
segundos = []
pos_x = []
pos_y = []
dr = []
lista_amarelo_x = []
lista_amarelo_y = []

## DATA ##

posicoes = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita.txt') 
centro_massa = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\direita_ponto_amarelo_henrique.txt')
tempo = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\tempo_henrique_direita.txt') 


with open(posicoes) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            pos_x.append(float(row[1]))
            pos_y.append(float(row[2]))
            dr.append(float(row[3]))

with open(centro_massa) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            lista_amarelo_x.append(float(row[0]))
            lista_amarelo_y.append(float(row[1]))
            Area_ref.append(float(row[2]))
            raio_ref.append(float(row[3]))
            

with open(tempo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            segundos.append(float(row[0]))


def novo_ref(lista_x, lista_y, ref_x, ref_y):

    ## Re-center the axis centerd on the yellow target

    lista_x_novo = []
    lista_y_novo = []

    for p in range(len(lista_x)):
        x_novo = lista_x[p] - ref_x[0]
        y_novo = lista_y[p] - ref_y[0]
        lista_x_novo.append(x_novo)
        lista_y_novo.append(y_novo)

    with open('henrique_esquerda_posicoes_novo_referencial.txt', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(['x', 'y'])
        csv_writer.writerows(zip(lista_x_novo, lista_y_novo))

    return(lista_x_novo, lista_y_novo)




novo_referencial = novo_ref(pos_x, pos_y, lista_amarelo_x, lista_amarelo_y)

new_pos_x = novo_referencial[0]
new_pos_y = novo_referencial[1]

############################################ Postion Normalization ##################################

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


##    print(lista_norm_x)
    with open('henrique_esquerda_posicoes_norm.txt', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(['x', 'y'])
        csv_writer.writerows(zip(lista_norm_x, lista_norm_y))


    return(lista_norm_x, lista_norm_y)


    
normalizacao = norm_pos(new_pos_x, new_pos_y)

pos_x_norm = normalizacao[0]
pos_y_norm = normalizacao[1]




