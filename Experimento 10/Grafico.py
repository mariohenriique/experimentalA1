import matplotlib.pyplot as plt
from scipy import stats

campo = []
tensao = []

arquivo = open('Exp 10 - Efeito Hall/dados2.txt','r')
arquivo.close

for linha in arquivo:
    campo.append(float(linha.split()[0]))
    tensao.append(float(linha.split()[1]))

x = tensao
y = campo
eixoy = []

slope, intercept, r, p, se = stats.linregress(x, y)
result = stats.linregress(x, y)
print(result.slope, result.stderr)

for i in tensao:
    eixoy.append(result.intercept + result.slope*i)

plt.scatter(x,y)
plt.plot(x,eixoy,'r')
plt.xlabel('Tensão (10^(-3) V)')
plt.ylabel('Corrente (10^(-3) A)')
plt.title('I x V')
plt.savefig('Exp 10 - Efeito Hall/grafico_corrente.png',format='png')
plt.show()