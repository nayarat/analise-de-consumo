# importanto bibliotecas necessárias para o processamento dos dados
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pegando o arquivo com os dados de 2016
maio_06 = np.genfromtxt('./consumo/2016/05-maio.csv', delimiter=';')
junho_06 = np.genfromtxt('./consumo/2016/06-junho.csv', delimiter=';')
julho_06 = np.genfromtxt('./consumo/2016/07-julho.csv', delimiter=';')
agosto_06 = np.genfromtxt('./consumo/2016/08-agosto.csv', delimiter=';')
setembro_06 = np.genfromtxt('./consumo/2016/09-setembro.csv', delimiter=';')
outubro_06 = np.genfromtxt('./consumo/2016/10-outubro.csv', delimiter=';')
novembro_06 = np.genfromtxt('./consumo/2016/11-novembro.csv', delimiter=';')
dezembro_06 = np.genfromtxt('./consumo/2016/12-dezembro.csv', delimiter=';')

# pegando o arquivo com os dados de 2017
janeiro_07 = np.genfromtxt('./consumo/2017/01-janeiro.csv', delimiter=';')
fevereiro_07 = np.genfromtxt('./consumo/2017/02-fevereiro.csv', delimiter=';')
marco_07 = np.genfromtxt('./consumo/2017/03-março.csv', delimiter=';')
abril_07 = np.genfromtxt('./consumo/2017/04-abril.csv', delimiter=';')
maio_07 = np.genfromtxt('./consumo/2017/05-maio.csv', delimiter=';')
junho_07 = np.genfromtxt('./consumo/2017/06-junho.csv', delimiter=';')

# passando os dados de consumo de 2016 para dataFrames
maio_06 = pd.DataFrame(maio_06[:, 2]).iloc[::-1].values
junho_06 = pd.DataFrame(junho_06[:, 2]).iloc[::-1].values
julho_06 = pd.DataFrame(julho_06[:, 2]).iloc[::-1].values
agosto_06 = pd.DataFrame(agosto_06[:, 2]).iloc[::-1].values
setembro_06 = pd.DataFrame(setembro_06[:, 2]).iloc[::-1].values
outubro_06 = pd.DataFrame(outubro_06[:, 2]).iloc[::-1].values
novembro_06 = pd.DataFrame(novembro_06[:, 2]).iloc[::-1].values
dezembro_06 = pd.DataFrame(dezembro_06[:, 2]).iloc[::-1].values

# passando os dados de consumo de 2017 para dataFrames
janeiro_07 = pd.DataFrame(janeiro_07[:, 2]).iloc[::-1].values
fevereiro_07 = pd.DataFrame(fevereiro_07[:, 2]).iloc[::-1].values
marco_07 = pd.DataFrame(marco_07[:, 2]).iloc[::-1].values
abril_07 = pd.DataFrame(abril_07[:, 2]).iloc[::-1].values
maio_07 = pd.DataFrame(maio_07[:, 2]).iloc[::-1].values
junho_07 = pd.DataFrame(junho_07[:, 2]).iloc[::-1].values


maio_06 = maio_06.iloc[::-1]
junho_06 = junho_06.iloc[::-1]
julho_06 = julho_06.iloc[::-1]
agosto_06 = agosto_06.iloc[::-1]
setembro_06 = setembro_06.iloc[::-1]
outubro_06 = outubro_06.iloc[::-1]
novembro_06 = novembro_06.iloc[::-1]
dezembro_06 = dezembro_06.iloc[::-1]

# passando os dados de consumo de 2017 para dataFrames
janeiro_07 = janeiro_07.iloc[::-1]
fevereiro_07 = fevereiro_07.iloc[::-1]
marco_07 = marco_07.iloc[::-1]
abril_07 = abril_07.iloc[::-1]
maio_07 = maio_07.iloc[::-1]
junho_07 = junho_07.iloc[::-1]


# retirando valores nulos de 2016
maio_06 = maio_06.dropna(axis=0, how='any')
junho_06 = junho_06.dropna(axis=0, how='any')
julho_06 = julho_06.dropna(axis=0, how='any')
agosto_06 = agosto_06.dropna(axis=0, how='any')
setembro_06 = setembro_06.dropna(axis=0, how='any')
outubro_06 = outubro_06.dropna(axis=0, how='any')
novembro_06 = novembro_06.dropna(axis=0, how='any')

# retirando valores nulos de 2017
janeiro_07 = janeiro_07.dropna(axis=0, how='any')
fevereiro_07 = fevereiro_07.dropna(axis=0, how='any')
marco_07 = marco_07.dropna(axis=0, how='any')
abril_07 = abril_07.dropna(axis=0, how='any')
maio_07 = maio_07.dropna(axis=0, how='any')
junho_07 = junho_07.dropna(axis=0, how='any')

# criando DataFrame de 2016
data2016 = pd.concat([maio_06, junho_06, julho_06, agosto_06,
                      setembro_06, outubro_06, novembro_06], ignore_index=True)

# criando DataFrame de 2017
data2017 = pd.concat([janeiro_07, fevereiro_07, marco_07,
                      abril_07, maio_07, junho_07], ignore_index=True)

# sum2017 = [janeiro_07.sum(), fevereiro_07.sum(), marco_07.sum(),
#            abril_07.sum(), maio_07.sum(), junho_07.sum()]

# plt.plot(sum2017)
# plt.show()

# plotando 2016
# plt.plot(maio_06)
# plt.title('grafico do mes de maio do ano de 2016')
# plt.show()
# plt.plot(junho_06)
# plt.title('grafico do mes de junho do ano de 2016')
# plt.show()
# plt.plot(julho_06)
# plt.title('grafico do mes de julho do ano de 2016')
# plt.show()
# plt.plot(agosto_06)
# plt.title('grafico do mes de agosto do ano de 2016')
# plt.show()
# plt.plot(setembro_06)
# plt.title('grafico do mes de setembro do ano de 2016')
# plt.show()
# plt.plot(outubro_06)
# plt.title('grafico do mes de outubro do ano de 2016')
# plt.show()
# plt.plot(novembro_06)
# plt.title('grafico do mes de novembro do ano de 2016')
# plt.show()
# plt.plot(data2016)
# plt.title('grafico do ano de 2016')
# plt.show()

# # plotando 2017
# plt.plot(janeiro_07)
# plt.title('grafico do mes de janeiro do ano de 2017')
plt.savefig('janeiro_07.png')
# plt.show()
# plt.plot(fevereiro_07)
# plt.title('grafico do mes de fevereiro do ano de 2017')
# plt.show()
# plt.plot(marco_07)
# plt.title('grafico do mes de marco do ano de 2017')
# plt.show()
# plt.plot(abril_07)
# plt.title('grafico do mes de abril do ano de 2017')
# plt.show()
# plt.plot(maio_07)
# plt.title('grafico do mes de maio do ano de 2017')
# plt.show()
# plt.plot(junho_07)
# plt.title('grafico do mes de junho do ano de 2017')
# plt.show()
# plt.plot(data2017)
# plt.show()

x = np.linspace(0, data2017.size, data2017.size)
plt.scatter(x, data2017)
plt.title('grafico do ano de 2017')
plt.show()
