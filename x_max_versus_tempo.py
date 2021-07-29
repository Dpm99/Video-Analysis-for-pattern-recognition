import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_1 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\henrique_direita_posicoes_norm.txt', delimiter ='\t')
df_1 = pd.DataFrame(df_1, columns = ['x', 'y'])


x_1 = df_1['x'].tolist()
y_1 = df_1['y'].tolist()

tempo_1 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Henrique\\Mao_direita_henrique\\tempo_henrique_direita.txt', delimiter ='\n')
tempo_1 = pd.DataFrame(tempo_1, columns = ['segundos'])
t_1 = tempo_1['segundos'].tolist()
##x_1_bin = np.array_split(x_1, 100)
##y_1_bin = np.array_split(y_1, 100)


df_2 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Andriy\\Mao_direita_andriy\\andriy_direita_posicoes_norm.txt')
df_2 = pd.DataFrame(df_2, columns = ['x', 'y'])

x_2 = df_2['x'].tolist()
y_2 = df_2['y'].tolist()

tempo_2 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Andriy\\Mao_direita_andriy\\tempo_andriy_direita.txt', delimiter ='\n')
tempo_2 = pd.DataFrame(tempo_1, columns = ['segundos'])
t_2 = tempo_1['segundos'].tolist()

##x_2_bin = np.array_split(x_2, 100)
##y_2_bin = np.array_split(y_2, 100)


df_3 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Calhau\\Mao_direita_calhau\\calhau_direita_posicoes_norm.txt')
df_3 = pd.DataFrame(df_3, columns = ['x', 'y'])

x_3 = df_3['x'].tolist()
y_3 = df_3['y'].tolist()

tempo_3 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Calhau\\Mao_direita_calhau\\tempo_calhau_direita.txt', delimiter ='\n')
tempo_3 = pd.DataFrame(tempo_1, columns = ['segundos'])
t_3 = tempo_1['segundos'].tolist()

##x_3_bin = np.array_split(x_3, 100)
##y_3_bin = np.array_split(y_3, 100)


df_4 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Fidalgo\\Mao_direita_fidalgo\\fidalgo_direita_posicoes_norm.txt')
df_4 = pd.DataFrame(df_4, columns = ['x', 'y'])


x_4 = df_4['x'].tolist()
y_4 = df_4['y'].tolist()

tempo_4 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Fidalgo\\Mao_direita_fidalgo\\tempo_fidalgo_direita.txt', delimiter ='\n')
tempo_4 = pd.DataFrame(tempo_1, columns = ['segundos'])
t_4 = tempo_1['segundos'].tolist()

##x_4_bin = np.array_split(x_4, 100)
##y_4_bin = np.array_split(y_4, 100)

df_5 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Nuno_Araujo\\Mao_direita_nuno\\nuno_araujo_direita_posicoes_norm.txt', delimiter ='\t')
df_5 = pd.DataFrame(df_5, columns = ['x', 'y'])


x_5 = df_5['x'].tolist()
y_5 = df_5['y'].tolist()

tempo_5 = pd.read_csv('C:\\Users\\DIOGO MOTA\\Desktop\\Codigo_Estagio\\DADOS\\Dados_Nuno_Araujo\\Mao_direita_nuno\\tempo_nuno_araujo_direita.txt', delimiter = '\n')
tempo_5 = pd.DataFrame(tempo_1, columns = ['segundos'])
t_5 = tempo_1['segundos'].tolist()

##x_5_bin = np.array_split(x_5, 100)
##y_5_bin = np.array_split(y_5, 100)

def maxi(lista):
    
    maximos =[]
    
    for i in range(len(lista)):

        if i ==0:
            maximos.append(abs(lista[0]))

        elif abs(lista[i]) > abs(lista[i-1]):
            maximos.append(abs(lista[i]))

        elif abs(lista[i]) <= abs(lista[i-1]):
            maximos.append(abs(lista[i-1]))              

    return(maximos)


x_1_max = maxi(x_1)
x_2_max = maxi(x_2)
x_3_max = maxi(x_3)
x_4_max = maxi(x_4)
x_5_max = maxi(x_5)

plt.subplot(241)
plt.plot(t_1, x_1_max, 'o')
plt.title('|x_max| em função do tempo (Henrique)')
plt.xlabel('t')
plt.ylabel('|x_max|')
plt.grid(True)

plt.subplot(245)
plt.semilogy(t_1, x_1_max, 'o')
plt.title('Log(|x_max|) em função do tempo (Henrique)')
plt.xlabel('t')
plt.ylabel('Log(|x_max|)')
plt.grid(True)

plt.subplot(242)
plt.plot(t_2, x_2_max, 'o')
plt.title('|x_max| em função do tempo (Andriy)')
plt.xlabel('t')
plt.ylabel('|x_max|')
plt.grid(True)

plt.subplot(246)
plt.semilogy(t_2, x_2_max, 'o')
plt.title('Log(|x_max|) em função do tempo (Andriy)')
plt.xlabel('t')
plt.ylabel('Log(|x_max|)')
plt.grid(True)

plt.subplot(243)
plt.plot(t_3, x_3_max, 'o')
plt.title('|x_max| em função do tempo (Miguel Calhau)')
plt.xlabel('t')
plt.ylabel('|x_max|')
plt.grid(True)

plt.subplot(247)
plt.semilogy(t_3, x_3_max, 'o')
plt.title('Log(|x_max|) em função do tempo (Miguel Calhau)')
plt.xlabel('t')
plt.ylabel('Log(|x_max|)')
plt.grid(True)

plt.subplot(244)
plt.plot(t_4, x_4_max, 'o')
plt.title('|x_max| em função do tempo (Miguel Fidalgo)')
plt.xlabel('t')
plt.ylabel('|x_max|')
plt.grid(True)

plt.subplot(248)
plt.semilogy(t_4, x_4_max, 'o')
plt.title('Log(|x_max|) em função do tempo (Miguel Fidalgo)')
plt.xlabel('t')
plt.ylabel('Log(|x_max|)')
plt.grid(True)

plt.subplot(255)
plt.plot(t_5, x_5_max, 'o')
plt.title('|x_max| em função do tempo (Nuno Araujo)')
plt.xlabel('t')
plt.ylabel('|x_max|')
plt.grid(True)

plt.subplot(259)
plt.semilogy(t_5, x_5_max, 'o')
plt.title('Log(|x_max|) em função do tempo (Nuno Aarujo)')
plt.xlabel('t')
plt.ylabel('Log(|x_max|)')
plt.grid(True)



plt.show()

















    
