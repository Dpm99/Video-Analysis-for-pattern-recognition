import matplotlib.pyplot as plt
import numpy as np
import cv2
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


segundos_esquerda = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\tempo_henrique_esquerda.txt')
direita = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita.txt')
amarelo_esquerda = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\esquerda_ponto_amarelo_henrique.txt')
esquerda = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\henrique_esquerda.txt')
esquerda_norm = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\henrique_esquerda_posicoes_norm.txt')
direita_norm = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_posicoes_norm.txt')
dt_1_direita = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_dt_threshold_1.txt')
dt_2_direita = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_dt_threshold_2.txt')
dt_0_5_direita = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_dt_threshold_0.5.txt')
dt_1_esquerda = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\henrique_esquerda_dt_threshold_1.txt')
dt_2_esquerda = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\henrique_esquerda_dt_threshold_2.txt')
dt_0_5_esquerda = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_esquerda_henrique\\henrique_esquerda_dt_threshold_0.5.txt')
amarelo_direita = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\direita_ponto_amarelo_henrique.txt')
segundos_direita = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\tempo_henrique_direita.txt')

pos_x_norm = []
pos_y_norm =[]


t_x_1 = []
dt_x_1 = []
t_y_1 = []
dt_y_1 = []

t_x_2 = []
dt_x_2 = []
t_y_2 = []
dt_y_2 = []

t_x_0_5 = []
dt_x_0_5 = []
t_y_0_5 = []
dt_y_0_5 = []


Area_ref = []
raio_ref = []
segundos = []
pos_x = []
pos_y = []
dr = []
lista_amarelo_x = []
lista_amarelo_y = []

with open(esquerda) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            pos_x.append(float(row[1]))
            pos_y.append(float(row[2]))
            dr.append(float(row[3]))
            

with open(amarelo_esquerda) as csv_file:
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
            

with open(segundos_esquerda) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            segundos.append(float(row[0]))


with open(dt_1_esquerda) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            t_x_1.append(float(row[0]))
            dt_x_1.append(float(row[1]))
            t_y_1.append(float(row[2]))
            dt_y_1.append(float(row[3]))
            

with open(dt_2_esquerda) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            t_x_2.append(float(row[0]))
            dt_x_2.append(float(row[1]))
            t_y_2.append(float(row[2]))
            dt_y_2.append(float(row[3]))
            


with open(dt_0_5_esquerda) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            t_x_0_5.append(float(row[0]))
            dt_x_0_5.append(float(row[1]))
            t_y_0_5.append(float(row[2]))
            dt_y_0_5.append(float(row[3]))

with open(esquerda_norm) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            pos_x_norm.append(float(row[0]))
            pos_y_norm.append(float(row[1]))
            
            



######Time Series#######
plt.plot(segundos, pos_x)
plt.grid(True)
plt.title('Série Temporal de x')
plt.xlabel('t (s)')
plt.ylabel('x')
##plt.savefig('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\Graficos\\Series_temporais\\nuno_araujo_serie_x_direita.png', dpi = 600, bbox_inches='tight')
plt.show()

plt.plot(segundos, pos_y)
plt.grid(True)
plt.title('Série Temporal de y')
plt.xlabel('t (s)')
plt.ylabel('y')
##plt.savefig('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\Graficos\\Series_temporais\\nuno_Araujo_serie_y_direita.png', dpi = 600, bbox_inches='tight')
plt.show()


######DT VS T#######
plt.subplot(231)
plt.plot(t_x_1, dt_x_1, 'o', color = 'r')
plt.grid(True)
plt.title('dt vs t com Threshold de 1 em x')
plt.xlabel('t')
plt.ylabel('dt')
plt.subplot(234)
plt.plot(segundos, pos_x_norm)
plt.axhline(1, 0, len(segundos), color = 'r')
plt.axhline(-1, 0, len(segundos), color = 'r')
plt.title('Série temporal de x normalizada, (Threshold = 1)')
plt.grid(True)
plt.xlabel('t (s)')
plt.ylabel('x')


plt.subplot(232)
plt.plot(t_x_2, dt_x_2, 's', color = 'orange')
plt.grid(True)
plt.title('dt vs t com Threshold de 2 em x')
plt.xlabel('t')
plt.ylabel('dt')
plt.subplot(235)
plt.plot(segundos, pos_x_norm)
plt.axhline(2, 0, len(segundos), color = 'orange')
plt.axhline(-2, 0, len(segundos), color = 'orange')
plt.title('Série temporal de x normalizada (Threshold = 2)')
plt.grid(True)
plt.xlabel('t (s)')
plt.ylabel('x')

plt.subplot(233)
plt.plot(t_x_0_5, dt_x_0_5, '^', color = 'g')
plt.grid(True)
plt.title('dt vs t com Threshold de 0.5 em x')
plt.xlabel('t')
plt.ylabel('dt')
plt.subplot(236)
plt.plot(segundos, pos_x_norm)
plt.axhline(0.5, 0, len(segundos), color = 'g')
plt.axhline(-0.5, 0, len(segundos), color = 'g')
plt.title('Série temporal de x normalizada (Threshold = 0.5)')
plt.grid(True)
plt.xlabel('t (s)')
plt.ylabel('x')


plt.show()






