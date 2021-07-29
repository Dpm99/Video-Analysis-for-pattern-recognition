import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


x_1_bin = np.array_split(x_1, 100)
y_1_bin = np.array_split(y_1, 100)

x_2_bin = np.array_split(x_2, 100)
y_2_bin = np.array_split(y_2, 100)

x_3_bin = np.array_split(x_3, 100)
y_3_bin = np.array_split(y_3, 100)

x_4_bin = np.array_split(x_4, 100)
y_4_bin = np.array_split(y_4, 100)

x_5_bin = np.array_split(x_5, 100)
y_5_bin = np.array_split(y_5, 100)

x_6_bin = np.array_split(x_6, 100)
y_6_bin = np.array_split(y_6, 100)

x_7_bin = np.array_split(x_7, 100)
y_7_bin = np.array_split(y_7, 100)

x_8_bin = np.array_split(x_8, 100)
y_8_bin = np.array_split(y_8, 100)

x_9_bin = np.array_split(x_9, 100)
y_9_bin = np.array_split(y_9, 100)

x_10_bin = np.array_split(x_10, 100)
y_10_bin = np.array_split(y_10, 100)

x_11_bin = np.array_split(x_11, 100)
y_11_bin = np.array_split(y_11, 100)

x_12_bin = np.array_split(x_12, 100)
y_12_bin = np.array_split(y_12, 100)


def MSD(lista):

    mean_squar_dis = []
    N = 0

    for i in range(len(lista)):
        
        N = len(lista[i])
        mean = np.mean(lista[i])
        somatorio = 0

        for j in range(len(lista[i])):

            somatorio += (lista[i][j] - mean)**2

        msd = somatorio / N

        mean_squar_dis.append(msd)

    return(mean_squar_dis)


msd_1 = MSD(x_1_bin)
msd_2 = MSD(x_2_bin)
msd_3 = MSD(x_3_bin)
msd_4 = MSD(x_4_bin)
msd_5 = MSD(x_5_bin)
msd_6 = MSD(x_6_bin)
msd_7 = MSD(x_7_bin)
msd_8 = MSD(x_8_bin)
msd_9 = MSD(x_9_bin)
msd_10 = MSD(x_10_bin)
msd_11 = MSD(x_11_bin)
msd_12 = MSD(x_12_bin)


plt.subplots_adjust(hspace = 0.3)
plt.subplot(341)
plt.plot(msd_1, 'o')
plt.title('MSD de x em função dos bins (Henrique)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)


plt.subplot(342)
plt.plot(msd_2, 'o', color = 'orange')
plt.title('MSD de x em função dos bins (Andriy)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)


plt.subplot(343)
plt.plot(msd_3, 'o', color = 'red')

plt.title('MSD de x em função dos bins (Miguel Calhau)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)


plt.subplot(344)
plt.plot(msd_4, 'o', color = 'green')

plt.title('MSD de x em função dos bins (Miguel Fidalgo)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(345)
plt.plot(msd_5, 'o', color = 'coral')
plt.title('MSD de x em função dos bins (Joana)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(346)
plt.plot(msd_6, 'o', color = 'darkkhaki')
plt.title('MSD de x em função dos bins (Diogo Mota)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(347)
plt.plot(msd_7, 'o', color = 'brown')
plt.title('MSD de x em função dos bins (Catarina Moura)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(348)
plt.plot(msd_8, 'o', color = 'slategray')
plt.title('MSD de x em função dos bins (Nuno Araujo)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(349)
plt.plot(msd_8, 'o', color = 'black')
plt.title('MSD de x em função dos bins (Ricardo)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(3,4,10)
plt.plot(msd_8, 'o', color = 'darkolivegreen')
plt.title('MSD de x em função dos bins (Tomas Alvim)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(3,4,11)
plt.plot(msd_10, 'o', color = 'peru')
plt.title('MSD de x em função dos bins (Tomas Sousa)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.subplot(3,4,12)
plt.plot(msd_12, 'o', color = 'darkviolet')
plt.title('MSD de x em função dos bins (Ze)')
plt.xlabel('bins')
plt.ylabel('MSD')
plt.grid(True)

plt.show()

        














        
    
