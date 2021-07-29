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

## Calculate the center of mass of the target

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

number_of_frames = 3307

lista_x = []
lista_y = []
lista_A = []
lista_r = []
   
for j in range(1, number_of_frames+1):
   print(j)

   original = cv2.imread('frame'+str(j)+'.jpg')
   #cv2.imshow('original',original)

   gamma = 1.5                                  # change the value here to get different result
   adjusted = adjust_gamma(original, gamma=gamma)
   #cv2.imshow("gammam image 1", adjusted)

   ##cv2.waitKey(0)
   ##cv2.destroyAllWindows()

   r_norm = adjusted[:,:,2]/255
   g_norm = adjusted[:,:,1]/255
   b_norm = adjusted[:,:,0]/255

   C = (1 - r_norm)
   M = (1 - g_norm)
   Y = (1 - b_norm)

   ##plt.imshow(Y)
   ##plt.show()

   media = Y.mean()

   aux = Y > media + 0.5

##   plt.imshow(aux)
##   plt.show()


   x1, y1 = np.nonzero(aux)
   lista_x.append(np.mean(x1))
   lista_y.append(np.mean(y1))

   #print(lista_x, lista_y)

   lista_A.append(np.count_nonzero(aux))
   lista_r.append(math.sqrt(lista_A[j-1] / math.pi))

   x = max(lista_y)   #####Invercao dos eixos 
   y = max(lista_x)   #####Invercao dos eixos
   A = max(lista_A)
   r = max(lista_r)




with open('esquerda_ponto_amarelo_henrique.txt', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['media x', 'media y','Area', 'raio'])
    csv_writer.writerow([x, y, A, r])




























