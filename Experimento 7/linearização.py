from scipy import stats
import numpy
import matplotlib.pyplot as plt

tensao = []
corrente = []
arquivo = open('Diodo Si.txt','r')
arquivo.close

for linha in arquivo:
    linha = linha.replace(',','.')
    tensao.append(float(linha.split()[0]))
    corrente.append(float(linha.split()[1]))
def linear(lista):
    ln = []
    for e in lista:
        if e == 0:
            e = e + 0.001
        elif e < 0:
            e = -e
        e = e*0.001
        ln.append(numpy.log(e))
    return ln
corrente = linear(corrente)

def multiplica(lista):
    mult = []
    for e in lista:
        mult.append(res.intercept + res.slope*e)
    return lista

x = tensao
y = corrente

slope, intercept, r, p, se = stats.linregress(x, y)
result = stats.linregress(x, y)
res = stats.linregress(x, y)
yregres = multiplica(tensao)

plt.scatter(x,y) #plotar o gráfico
plt.plot(x, yregres, 'r', label='fitted line')
plt.title ('Regressão Linear') #título
plt.xlabel('Tensão (V)') #título do eixo x
plt.ylabel('ln(Corrente) (A)') #título do eixo y
plt.savefig('grafico_regressao.png',format='png')
plt.show()

print(result.intercept, result.intercept_stderr)