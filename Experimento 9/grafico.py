import matplotlib.pyplot as plt
from scipy import stats

raio = []
tensao = []
corrente = []

arquivo = open('dados005.txt','r')
arquivo.close

for linha in arquivo:
    raio.append(float(linha.split()[0]))
    tensao.append(float(linha.split()[1]))
    corrente.append(float(linha.split()[2]))

x = tensao
y = []
eixoy = []

for i in corrente:
    y.append(124*1.26*10**(-6)*i/(1.25**1.5*29.5))

slope, intercept, r, p, se = stats.linregress(x, y)
result = stats.linregress(x, y)
print(result.slope, result.stderr)

for i in tensao:
    eixoy.append(result.intercept + result.slope*i)

plt.scatter(x,y)
plt.plot(x,eixoy,'r')
plt.xlabel('Tensão (V)')
plt.ylabel('Campo magnético ao quadrado (T²)')
plt.title('B² x V (raio 5cm)')
plt.savefig('grafico_raio5.png',format='png')
plt.show()