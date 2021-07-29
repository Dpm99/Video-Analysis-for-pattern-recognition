import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##df_1 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita.csv')
##df_1 = pd.DataFrame(df_1, columns = ['frames', 'x', 'y', 'dr'])
##df_1 = df_1.drop([0])
##
##x_1 = df_1['x'].tolist()
##y_1 = df_1['y'].tolist()

##df_11 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_posicoes_norm.txt', delimiter ='\t')
##df_11 = pd.DataFrame(df_11, columns = ['x', 'y'])
##
##
##x_11 = df_11['x'].tolist()
##y_11 = df_11['y'].tolist()
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


def velocidade(lista):
    ## calculates the speed of the laser between frames
    lista_v =[0]

    for i in range(0, len(lista)-1):
        
        dt = 1/3

        v = (lista[i] - lista[i+1])/dt
        lista_v.append(v)
    return(lista_v)


v_x_1 = velocidade(x_1)
v_y_1 = velocidade(y_1)

v_x_11 = velocidade(x_11)
v_y_11 = velocidade(y_11)
                    

v_x_2 = velocidade(x_2)
v_y_2 = velocidade(y_2)

v_x_3 = velocidade(x_3)
v_y_3 = velocidade(y_3)

v_x_4 = velocidade(x_4)
v_y_4 = velocidade(y_4)

v_x_5 = velocidade(x_5)
v_y_5 = velocidade(y_5)

v_x_6 = velocidade(x_6)
v_y_6 = velocidade(y_6)

v_x_7 = velocidade(x_7)
v_y_7 = velocidade(y_7)

v_x_8 = velocidade(x_8)
v_y_8 = velocidade(y_8)

v_x_9 = velocidade(x_9)
v_y_9= velocidade(y_9)

v_x_10 = velocidade(x_10)
v_y_10 = velocidade(y_10)

v_x_11 = velocidade(x_11)
v_y_11 = velocidade(y_11)

v_x_12 = velocidade(x_12)
v_y_12 = velocidade(y_12)

## Plot of the Phase space


plt.subplot(241)
plt.plot(v_x_1, x_1, 'o', markersize = 3)
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Henrique)')
plt.grid(True)

plt.subplot(245)
plt.plot(v_y_1, y_1, 'o', markersize = 3 )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Henrique)')


plt.subplot(242)
plt.plot(v_x_2, x_2, 'o', markersize = 3, color = 'orange')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Andriy)')
plt.grid(True)

plt.subplot(246)
plt.plot(v_y_2, y_2, 'o', markersize = 3, color = 'orange' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Andriy)')


plt.subplot(243)
plt.plot(v_x_3, x_3, 'o', markersize = 3, color = 'r')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Miguel Calhau)')
plt.grid(True)

plt.subplot(247)
plt.plot(v_y_3, y_3, 'o', markersize = 3, color = 'r' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Miguel Calhau)')

plt.subplot(244)
plt.plot(v_x_4, x_4, 'o', markersize = 3, color = 'khaki')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Miguel Fidalgo)')
plt.grid(True)

plt.subplot(248)
plt.plot(v_y_4, y_4, 'o', markersize = 3, color = 'khaki' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Miguel Fidalgo)')

plt.show()

plt.subplot(241)
plt.plot(v_x_5, x_5, 'o', markersize = 3, color = 'green')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Joana)')
plt.grid(True)

plt.subplot(245)
plt.plot(v_y_5, y_5, 'o', markersize = 3, color = 'green' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Joana)')

plt.subplot(242)
plt.plot(v_x_6, x_6, 'o', markersize = 3, color = 'blue')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Diogo Mota)')
plt.grid(True)

plt.subplot(246)
plt.plot(v_y_6, y_6, 'o', markersize = 3, color = 'blue' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Diogo Mota)')

plt.subplot(243)
plt.plot(v_x_7, x_7, 'o', markersize = 3, color = 'orange')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Catarina Moura)')
plt.grid(True)

plt.subplot(247)
plt.plot(v_y_7, y_7, 'o', markersize = 3, color = 'orange' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Catarina Moura)')

plt.subplot(244)
plt.plot(v_x_8, x_8, 'o', markersize = 3, color = 'coral')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Nuno Araújo)')
plt.grid(True)

plt.subplot(248)
plt.plot(v_y_8, y_8, 'o', markersize = 3, color = 'coral' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Nuno Araújo)')

plt.show()

plt.subplot(241)
plt.plot(v_x_9, x_9, 'o', markersize = 3, color = 'slategray')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Ricardo)')
plt.grid(True)

plt.subplot(245)
plt.plot(v_y_9, y_9, 'o', markersize = 3, color = 'slategray' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Ricardo)')


plt.subplot(242)
plt.plot(v_x_10, x_10, 'o', markersize = 3, color = 'brown')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Tomas Alvim)')
plt.grid(True)

plt.subplot(246)
plt.plot(v_y_10, y_10, 'o', markersize = 3, color = 'brown' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Tomas Alvim)')

plt.subplot(243)
plt.plot(v_x_11, x_11, 'o', markersize = 3, color = 'darkkhaki')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Tomas Sousa)')
plt.grid(True)

plt.subplot(247)
plt.plot(v_y_11, y_11, 'o', markersize = 3, color = 'darkkhaki' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Tomas Sousa)')

plt.subplot(244)
plt.plot(v_x_7, x_7, 'o', markersize = 3, color = 'darkgoldenrod')
plt.xlabel('v_x')
plt.ylabel('x')
plt.title('Espaço de Fase de x (Ze)')
plt.grid(True)

plt.subplot(248)
plt.plot(v_y_12, y_12, 'o', markersize = 3, color = 'darkgoldenrod' )
plt.grid(True)
plt.xlabel('v_y')
plt.ylabel('y')
plt.title('Espaço de Fase de y (Ze)')

plt.show()

