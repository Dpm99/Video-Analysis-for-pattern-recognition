import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df_1 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_posicoes_norm.txt', delimiter ='\t')
df_1 = pd.DataFrame(df_1, columns = ['x', 'y'])


x_1 = df_1['x'].tolist()
y_1 = df_1['y'].tolist()

df_2 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Andriy\\Mao_direita_andriy\\andriy_direita_posicoes_norm.txt')
df_2 = pd.DataFrame(df_2, columns = ['x', 'y'])


x_2 = df_2['x'].tolist()
y_2 = df_2['y'].tolist()

df_3 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Calhau\\Mao_direita_calhau\\calhau_direita_posicoes_norm.txt')
df_3 = pd.DataFrame(df_3, columns = ['x', 'y'])


x_3 = df_3['x'].tolist()
y_3 = df_3['y'].tolist()

df_4 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Fidalgo\\Mao_direita_fidalgo\\fidalgo_direita_posicoes_norm.txt')
df_4 = pd.DataFrame(df_4, columns = ['x', 'y'])


x_4 = df_4['x'].tolist()
y_4 = df_4['y'].tolist()

df_5 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Joana\\Mao_direita_joana\\joana_direita_posicoes_norm.txt')
df_5 = pd.DataFrame(df_5, columns = ['x', 'y'])


x_5 = df_5['x'].tolist()
y_5 = df_5['y'].tolist()

df_6 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Mota\\Mao_direita_mota\\diogo_direita_posicoes_norm.txt')
df_6 = pd.DataFrame(df_6, columns = ['x', 'y'])


x_6 = df_6['x'].tolist()
y_6 = df_6['y'].tolist()

df_7 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Moura\\Mao_direita_moura\\catarina_direita_posicoes_norm.txt')
df_7 = pd.DataFrame(df_7, columns = ['x', 'y'])


x_7 = df_7['x'].tolist()
y_7 = df_7['y'].tolist()

df_8 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Nuno_Araujo\\Mao_direita_nuno\\nuno_araujo_direita_posicoes_norm.txt', delimiter = '\t')
df_8 = pd.DataFrame(df_8, columns = ['x', 'y'])

x_8 = df_8['x'].tolist()
y_8 = df_8['y'].tolist()

df_9 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Ricardo\\Mao_direita_ricardo\\ricardo_direita_posicoes_norm.txt')
df_9 = pd.DataFrame(df_9, columns = ['x', 'y'])

x_9 = df_9['x'].tolist()
y_9= df_9['y'].tolist()

df_10 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Tomas_Alvim\\Mao_direita_alvim\\alvim_direita_posicoes_norm.txt')
df_10 = pd.DataFrame(df_10, columns = ['x', 'y'])

x_10 = df_10['x'].tolist()
y_10 = df_10['y'].tolist()

df_11 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Tomas_Sousa\\Mao_direita_tomas_sousa\\tomas_sousa_direita_posicoes_norm.txt', delimiter = '\t')
df_11 = pd.DataFrame(df_11, columns = ['x', 'y'])

x_11= df_11['x'].tolist()
y_11 = df_11['y'].tolist()

df_12 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Ze\\Mao_direita_ze\\ze_direita_posicoes_norm.txt')
df_12 = pd.DataFrame(df_12, columns = ['x', 'y'])

x_12 = df_12['x'].tolist()
y_12 = df_12['y'].tolist()


bins = 50

x_1_bin = np.array_split(x_1, bins)
y_1_bin = np.array_split(y_1, bins)

x_2_bin = np.array_split(x_2, bins)
y_2_bin = np.array_split(y_2, bins)

x_3_bin = np.array_split(x_3, bins)
y_3_bin = np.array_split(y_3, bins)

x_4_bin = np.array_split(x_4, bins)
y_4_bin = np.array_split(y_4, bins)

x_5_bin = np.array_split(x_5, bins)
y_5_bin = np.array_split(y_5, bins)

x_6_bin = np.array_split(x_6, bins)
y_6_bin = np.array_split(y_6, bins)

x_7_bin = np.array_split(x_7, bins)
y_7_bin = np.array_split(y_7, bins)

x_8_bin = np.array_split(x_8, bins)
y_8_bin = np.array_split(y_8, bins)

x_9_bin = np.array_split(x_9, bins)
y_9_bin = np.array_split(y_9, bins)

x_10_bin = np.array_split(x_10, bins)
y_10_bin = np.array_split(y_10, bins)

x_11_bin = np.array_split(x_11, bins)
y_11_bin = np.array_split(y_11, bins)

x_12_bin = np.array_split(x_12, bins)
y_12_bin = np.array_split(y_12, bins)

def probabilidade(lista, threshold):
    'Calculates the probability of the laser leaving the threshold area in each bin'

    
    lista_prob =[]
    media = []
    
    for i in range(len(lista)):
        
        pontos_fora = 0

        for j in range(len(lista[i])):

            if abs(lista[i][j]) >threshold:

                pontos_fora +=1
                
            else:
                continue

        prob = pontos_fora / len(lista[i])
        mean = np.mean(lista[i])
        media.append(mean)
        lista_prob.append(prob)
        
    return(lista_prob, media)


thresh = 1.5

probabilidade_1 = probabilidade(x_1_bin, thresh)
probabilidade_2 = probabilidade(x_2_bin, thresh)
probabilidade_3 = probabilidade(x_3_bin, thresh)
probabilidade_4 = probabilidade(x_4_bin, thresh)
probabilidade_5 = probabilidade(x_5_bin, thresh)
probabilidade_6 = probabilidade(x_6_bin, thresh)
probabilidade_7 = probabilidade(x_7_bin, thresh)
probabilidade_8 = probabilidade(x_8_bin, thresh)
probabilidade_9 = probabilidade(x_9_bin, thresh)
probabilidade_10 = probabilidade(x_10_bin, thresh)
probabilidade_11 = probabilidade(x_11_bin, thresh)
probabilidade_12 = probabilidade(x_12_bin, thresh)


probabilidade_1_y = probabilidade(y_1_bin, thresh)
probabilidade_2_y = probabilidade(y_2_bin, thresh)
probabilidade_3_y = probabilidade(y_3_bin, thresh)
probabilidade_4_y = probabilidade(y_4_bin, thresh)
probabilidade_5_y = probabilidade(y_5_bin, thresh)
probabilidade_6_y = probabilidade(y_6_bin, thresh)
probabilidade_7_y = probabilidade(y_7_bin, thresh)
probabilidade_8_y = probabilidade(y_8_bin, thresh)
probabilidade_9_y = probabilidade(y_9_bin, thresh)
probabilidade_10_y = probabilidade(y_10_bin, thresh)
probabilidade_11_y = probabilidade(y_11_bin, thresh)
probabilidade_12_y = probabilidade(y_12_bin, thresh)

def menos_log(lista):

    'Converte a lista de probabilidades no simetrico do logaritmo do valor da probabilidade'
    
    log_prob =[]
    
    for j in range(len(lista)):

        valor = np.log(lista[j])
        log_prob.append(valor)

    return(log_prob)


log_1 = menos_log(probabilidade_1[0])
log_2 = menos_log(probabilidade_2[0])
log_3 = menos_log(probabilidade_3[0])
log_4 = menos_log(probabilidade_4[0])
log_5 = menos_log(probabilidade_5[0])
log_6 = menos_log(probabilidade_6[0])
log_7 = menos_log(probabilidade_7[0])
log_8 = menos_log(probabilidade_8[0])
log_9 = menos_log(probabilidade_9[0])
log_10 = menos_log(probabilidade_10[0])
log_11 = menos_log(probabilidade_11[0])
log_12 = menos_log(probabilidade_12[0])

log_1_y = menos_log(probabilidade_1_y[0])
log_2_y = menos_log(probabilidade_2_y[0])
log_3_y = menos_log(probabilidade_3_y[0])
log_4_y = menos_log(probabilidade_4_y[0])
log_5_y = menos_log(probabilidade_5_y[0])
log_6_y = menos_log(probabilidade_6_y[0])
log_7_y = menos_log(probabilidade_7_y[0])
log_8_y = menos_log(probabilidade_8_y[0])
log_9_y = menos_log(probabilidade_9_y[0])
log_10_y = menos_log(probabilidade_10_y[0])
log_11_y = menos_log(probabilidade_11_y[0])
log_12_y = menos_log(probabilidade_12_y[0])


plt.subplots_adjust(hspace = 0.3)
plt.subplot(341)
plt.plot(probabilidade_1[1], log_1, 'o')
plt.title('- Log(P(x)) em função de x (Henrique)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(342)
plt.plot(probabilidade_2[1], log_2, 'o', color = 'red')
plt.title('- Log(P(x)) em função de x (Andriy)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(343)
plt.plot(probabilidade_3[1], log_3, 'o', color = 'orange')
plt.title('- Log(P(x)) em função de x (Miguel Calhau)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(344)
plt.plot(probabilidade_4[1], log_4, 'o', color = 'green')
plt.title('- Log(P(x)) em função de x (Miguel Fidalgo)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(345)
plt.plot(probabilidade_5[1], log_5, 'o', color = 'coral')
plt.title('- Log(P(x)) em função de x (Joana)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(346)
plt.plot(probabilidade_6[1], log_6, 'o', color = 'Black')
plt.title('- Log(P(x)) em função de x (Diogo Mota)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(347)
plt.plot(probabilidade_7[1], log_7, 'o', color = 'darkkhaki')
plt.title('- Log(P(x)) em função de x (Catarina Moura)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(348)
plt.plot(probabilidade_8[1], log_8, 'o', color = 'slategray')
plt.title('- Log(P(x)) em função de x (Nuno Araújo)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(349)
plt.plot(probabilidade_9[1], log_9, 'o', color = 'pink')
plt.title('- Log(P(x)) em função de x (Ricardo)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(3,4,10)
plt.plot(probabilidade_10[1], log_10, 'o', color = 'olivedrab')
plt.title('- Log(P(x)) em função de x (Tomás Alvim)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

##x_cos = np.arange(-3,2*np.pi,0.1)   
##y_cos = 2*np.cos(3*x_cos/1.4 - math.pi)


plt.subplot(3,4,11)
plt.plot(probabilidade_11[1], log_11, 'o', color = 'gold')
##plt.plot(x_cos, y_cos-2.2)
plt.title('- Log(P(x)) em função de x (Tomás Sousa)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(3,4,12)
plt.plot(probabilidade_12[1], log_12, 'o', color = 'brown')
plt.title('- Log(P(x)) em função de x (Ze)')
plt.xlabel('x')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.show()


##################################################################For y####################################
############################################################################################################

plt.subplots_adjust(hspace = 0.3)
plt.subplot(341)
plt.plot(probabilidade_1_y[1], log_1_y, 'o')
plt.title('- Log(P(y)) em função de y (Henrique)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(342)
plt.plot(probabilidade_2_y[1], log_2_y, 'o', color = 'red')
plt.title('- Log(P(y)) em função de y (Andriy)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(343)
plt.plot(probabilidade_3_y[1], log_3_y, 'o', color = 'orange')
plt.title('- Log(P(x)) em função de y (Miguel Calhau)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(344)
plt.plot(probabilidade_4_y[1], log_4_y, 'o', color = 'green')
plt.title('- Log(P(y)) em função de y (Miguel Fidalgo)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(345)
plt.plot(probabilidade_5_y[1], log_5_y, 'o', color = 'coral')
plt.title('- Log(P(y)) em função de y (Joana)')
plt.xlabel('y')
plt.ylabel('- Log(P(x))')
plt.grid(True)

plt.subplot(346)
plt.plot(probabilidade_6_y[1], log_6_y, 'o', color = 'Black')
plt.title('- Log(P(y)) em função de y (Diogo Mota)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(347)
plt.plot(probabilidade_7_y[1], log_7_y, 'o', color = 'darkkhaki')
plt.title('- Log(P(y)) em função de y (Catarina Moura)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(348)
plt.plot(probabilidade_8_y[1], log_8_y, 'o', color = 'slategray')
plt.title('- Log(P(y)) em função de y (Nuno Araújo)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(349)
plt.plot(probabilidade_9_y[1], log_9_y, 'o', color = 'pink')
plt.title('- Log(P(y)) em função de y (Ricardo)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(3,4,10)
plt.plot(probabilidade_10_y[1], log_10_y, 'o', color = 'olivedrab')
plt.title('- Log(P(y)) em função de y (Tomás Alvim)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)



plt.subplot(3,4,11)
plt.plot(probabilidade_11_y[1], log_11_y, 'o', color = 'gold')

plt.title('- Log(P(y)) em função de y (Tomás Sousa)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.subplot(3,4,12)
plt.plot(probabilidade_12_y[1], log_12_y, 'o', color = 'brown')
plt.title('- Log(P(y)) em função de y (Ze)')
plt.xlabel('y')
plt.ylabel('- Log(P(y))')
plt.grid(True)

plt.show()
    
    


