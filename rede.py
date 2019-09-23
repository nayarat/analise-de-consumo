#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


maio_06 = np.genfromtxt('./consumo/2016/05-maio.csv', delimiter=';')
junho_06 = np.genfromtxt('./consumo/2016/06-junho.csv', delimiter=';')
julho_06 = np.genfromtxt('./consumo/2016/07-julho.csv', delimiter=';')
agosto_06 = np.genfromtxt('./consumo/2016/08-agosto.csv', delimiter=';')
setembro_06 = np.genfromtxt('./consumo/2016/09-setembro.csv', delimiter=';')
outubro_06 = np.genfromtxt('./consumo/2016/10-outubro.csv', delimiter=';')
novembro_06 = np.genfromtxt('./consumo/2016/11-novembro.csv', delimiter=';')
dezembro_06 = np.genfromtxt('./consumo/2016/12-dezembro.csv', delimiter=';')


# In[3]:


janeiro_07 = np.genfromtxt('./consumo/2017/01-janeiro.csv', delimiter=';')
fevereiro_07 = np.genfromtxt('./consumo/2017/02-fevereiro.csv', delimiter=';')
marco_07 = np.genfromtxt('./consumo/2017/03-março.csv', delimiter=';')
abril_07 = np.genfromtxt('./consumo/2017/04-abril.csv', delimiter=';')
maio_07 = np.genfromtxt('./consumo/2017/05-maio.csv', delimiter=';')
junho_07 = np.genfromtxt('./consumo/2017/06-junho.csv', delimiter=';')


# In[4]:


maio_06 = pd.DataFrame(maio_06[:, 2])
junho_06 = pd.DataFrame(junho_06[:, 2])
julho_06 = pd.DataFrame(julho_06[:, 2])
agosto_06 = pd.DataFrame(agosto_06[:, 2])
setembro_06 = pd.DataFrame(setembro_06[:, 2])
outubro_06 = pd.DataFrame(outubro_06[:, 2])
novembro_06 = pd.DataFrame(novembro_06[:, 2])
dezembro_06 = pd.DataFrame(dezembro_06[:, 2])


# In[5]:


janeiro_07 = pd.DataFrame(janeiro_07[:, 2])
fevereiro_07 = pd.DataFrame(fevereiro_07[:, 2])
marco_07 = pd.DataFrame(marco_07[:, 2])
abril_07 = pd.DataFrame(abril_07[:, 2])
maio_07 = pd.DataFrame(maio_07[:, 2])
junho_07 = pd.DataFrame(junho_07[:, 2])


# In[6]:


media_maio_06 = maio_06.mean()
maio_06.update(maio_06.fillna(media_maio_06))
media_junho_06 = junho_06.mean()
junho_06.update(junho_06.fillna(media_junho_06))
media_julho_06 = julho_06.mean()
julho_06.update(julho_06.fillna(media_julho_06))
media_agosto_06 = agosto_06.mean()
agosto_06.update(agosto_06.fillna(media_agosto_06))
media_setembro_06 = setembro_06.mean()
setembro_06.update(setembro_06.fillna(media_setembro_06))
media_outubro_06 = outubro_06.mean()
outubro_06.update(outubro_06.fillna(media_outubro_06))
media_novembro_06 = novembro_06.mean()
novembro_06.update(novembro_06.fillna(media_novembro_06))
media_dezembro_06 = dezembro_06.mean()
dezembro_06.update(dezembro_06.fillna(media_dezembro_06))


# In[7]:


media_janeiro_07 = janeiro_07.mean()
janeiro_07.update(janeiro_07.fillna(media_janeiro_07))
media_fevereiro_07 = fevereiro_07.mean()
fevereiro_07.update(fevereiro_07.fillna(media_fevereiro_07))
media_marco_07 = marco_07.mean()
marco_07.update(marco_07.fillna(media_marco_07))
media_abril_07 = abril_07.mean()
abril_07.update(abril_07.fillna(media_abril_07))
media_maio_07 = maio_07.mean()
maio_07.update(maio_07.fillna(media_maio_07))
media_junho_07 = junho_07.mean()
junho_07.update(junho_07.fillna(media_junho_07))


# In[8]:


janeiro_07


# In[9]:


maio_06 = maio_06.iloc[::-1]
junho_06 = junho_06.iloc[::-1]
julho_06 = julho_06.iloc[::-1]
agosto_06 = agosto_06.iloc[::-1]
setembro_06 = setembro_06.iloc[::-1]
outubro_06 = outubro_06.iloc[::-1]
novembro_06 = novembro_06.iloc[::-1]
dezembro_06 = dezembro_06.iloc[::-1]


# In[10]:


janeiro_07 = janeiro_07.iloc[::-1]
fevereiro_07 = fevereiro_07.iloc[::-1]
marco_07 = marco_07.iloc[::-1]
abril_07 = abril_07.iloc[::-1]
maio_07 = maio_07.iloc[::-1]
junho_07 = junho_07.iloc[::-1]


# In[11]:


# criando DataFrame de 2016
data2016 = pd.concat([maio_06, junho_06, julho_06, agosto_06,
                      setembro_06, outubro_06, novembro_06], ignore_index=True)

# criando DataFrame de 2017
data2017 = pd.concat([janeiro_07, fevereiro_07, marco_07,
                      abril_07, maio_07, junho_07], ignore_index=True)


# In[12]:


# plotando 2016
plt.figure(figsize=(20, 10))
plt.plot(maio_06)
plt.plot(junho_06)
plt.plot(julho_06)
plt.plot(agosto_06)
plt.plot(setembro_06)
plt.plot(outubro_06)
plt.plot(novembro_06)
plt.show()


# In[13]:


plt.figure(figsize=(20, 10))
plt.plot(data2016)
plt.title('grafico do ano de 2016')
plt.show()


# In[14]:


# plotando 2017
plt.figure(figsize=(20, 10))
plt.plot(janeiro_07)
plt.plot(fevereiro_07)
plt.plot(marco_07)
plt.plot(abril_07)
plt.plot(maio_07)
plt.plot(junho_07)


# In[15]:


plt.figure(figsize=(20, 10))
plt.plot(data2017)
plt.title('grafico do ano de 2016')
plt.show()


# In[16]:


data2017.size


# In[17]:


x = np.linspace(0, data2017.size-1, data2017.size)


# In[18]:


x.size


# In[19]:


x = x.reshape(x.size, 1)


# In[20]:


x.shape


# In[21]:


grauDoPolinomio = 5


# In[22]:


#-------------------------------Biblioteca------------------------------------#

#--------------------Elevando as entradas a ordem degree----------------------#
# cada atributo será elevado a 1, 2, 3 e 4 criando assim 3 novos atributos, esse número é definido por escolha do programador
poly = PolynomialFeatures(degree=grauDoPolinomio)
x = poly.fit_transform(x)


# In[23]:


#---------------------------Criando o regressor-------------------------------#
regressor = LinearRegression()
regressor.fit(x, data2017)


# In[24]:


#----Ver a correlação do modelo com relação a base de dados de Treinamento----#
score = regressor.score(x, data2017)
print('A correlação do modelo com a base de dados de treinamento é de: {}'.format(score))


# In[25]:


#------------------------------Prevendo um valor------------------------------#
previsoes = regressor.predict(x)

#------------------Diferança entre valores reais e previstos------------------#
erro_absoluto = mean_absolute_error(data2017, previsoes)
erro_quadratico = mean_squared_error(data2017, previsoes)
print('Erro absoluto: {}'.format(erro_absoluto))
print('Erro quadratico: {}'.format(erro_quadratico))


# In[26]:


plt.figure(figsize=(20, 10))
plt.plot(data2017)
plt.plot(previsoes, 'red')
plt.show()


# In[27]:


valores = np.linspace(15261, 15261+20000, 15261+20000+1)


# In[28]:


valores = valores.reshape(valores.size, 1)


# In[29]:


valores = poly.transform(valores)


# In[30]:


novas_previsoes = regressor.predict(valores)


# In[31]:


plt.figure(figsize=(20, 10))
plt.plot(novas_previsoes)


# In[32]:


novas_previsoes[5000]
