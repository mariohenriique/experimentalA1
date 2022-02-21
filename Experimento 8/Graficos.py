import matplotlib.pyplot as plt

time = []
voltage_resistor = []
time2 = []
voltage_capacitor = []
voltagea = []
voltageb = []
histe = []
campo = []

arquivo = open('voltage_A.txt','r')
arquivo2 = open('voltage_B.txt','r')
arquivo3 = open('XY.txt','r')
arquivo.close
arquivo2.close
arquivo3.close

for linha in arquivo:
    time.append(float(linha.split()[0]))
    voltage_resistor.append(float(linha.split()[1]))

for linha in arquivo2:
    time2.append(float(linha.split()[0]))
    voltage_capacitor.append(float(linha.split()[1]))

for linha in arquivo3:
    voltagea.append(float(linha.split()[0]))
    voltageb.append(float(linha.split()[1]))

x = voltage_resistor
y = voltage_capacitor

for i in voltagea:
    h = i*1000*1.26*10**(-6)/(2*0.03*56)
    histe.append(h)

for i in voltageb:
    b = i*1000000*10*10**(-6)/(10000*0.04*0.04)
    campo.append(b)
x1 = histe
y1 = campo

plt.scatter(x1,y1)
plt.title('Curva de histerese canal A X canal B')
plt.xlabel('H' + "'" + '(T)')
plt.ylabel('B (V)')
plt.grid()
plt.savefig('grafico_H_B.png',format = 'png')
plt.show()