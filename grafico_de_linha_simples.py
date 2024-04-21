from matplotlib import pyplot as plt
#Linha horizontal
years = [1950, 1960, 1970, 1980, 1990, 2000, 2001]
#linha vertical
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#criar um grafico de linhas 
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#Adicionar um titulo no grafico 
plt.title("Nominal GDP") 

#Adicionar um titulo no eixo 
plt.ylabel("billions of $")
plt.show()







