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

posicoes_normalizadas = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_posicoes_norm.txt')
tempo = Path('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\tempo_henrique_direita.txt') 

pos_x_norm = []
pos_y_norm = []
segundos = []

with open(posicoes_normalizadas) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            pos_x_norm.append(float(row[0]))
            pos_y_norm.append(float(row[1]))
            


with open(tempo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    counter=0
    for row in csv_reader:
        if counter == 0:
            counter +=1
        else:
            segundos.append(float(row[0]))

            

def delta_t(thresh, lista_x, lista_y, segundos):
    'Calculates the dt where the normalised positions are >1'
    dt_x = []      #####dt where the positions is above 1 or below -1
    tempo_x = []   #####first instant where the position is above 1 or below -1
    tf_x = []   ####last instant where the position is above 1 or below -1

    for i in range(len(lista_x)):
        if i == 0 and (lista_x[i] > thresh or lista_x[i] < - thresh):
    ##        print(segundos[i])
            tempo_x.append(segundos[i])
        
            
        elif (lista_x[i] > thresh and lista_x[i - 1] <= thresh) or (lista_x[i] < - thresh and lista_x[i-1] >= - thresh):
    ##        print(segundos[i])
            tempo_x.append(segundos[i])

    for k in range(len(lista_x)-1):
        if (lista_x[k] > thresh and lista_x[k+1] <= thresh) or (lista_x[k] < - thresh and lista_x[k+1] >= - thresh):
            tf_x.append(segundos[k+1])
            
    if len(tf_x) < len(tempo_x):
        tf_x.append(segundos[-1])
        

    for j in range(len(tempo_x)):

        dt_x.append(tf_x[j] - tempo_x[j])


    dt_y =  []
    tf_y = []
    tempo_y = []

    for m in range(len(lista_y)):
        if m == 0 and (lista_y[m] > thresh or lista_y[m] < - thresh):
            
            tempo_y.append(segundos[m])
        
            
        elif (lista_y[m] > thresh and lista_y[m - 1] <= thresh) or (lista_y[m] < - thresh and lista_y[m-1] >= - thresh):

            tempo_y.append(segundos[m])

    for l in range(len(lista_y)-1):
        if (lista_y[l] > thresh and lista_y[l+1] <= thresh) or (lista_y[l] < - thresh and lista_y[l+1] >= - thresh):
            tf_y.append(segundos[l+1])
            
    if len(tf_y) < len(tempo_y):
        tf_y.append(segundos[-1])
        

    for n in range(len(tempo_y)):

        dt_y.append(tf_y[n] - tempo_y[n])
        

    with open('henrique_direita_dt_threshold_2.txt', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(['tempo_x', 'dt_x', 'tempo_y', 'dt_y'])
        csv_writer.writerows(zip(tempo_x, dt_x, tempo_y, dt_y))

    return(dt_x, dt_y, tempo_x, tempo_y)


int_tempo = delta_t(2, pos_x_norm, pos_y_norm, segundos)


    
