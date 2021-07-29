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
## Separate video into frames

tempo = []
frames = []
number_of_frames = 3181


for i in range(1, number_of_frames+1):

    segundos  = i * (1/30)
    tempo.append(segundos)

print(len(tempo))

with open('tempo_ze_esquerda.txt', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\n')
    csv_writer.writerow(['segundos'])
    csv_writer.writerow(tempo)





                
                
