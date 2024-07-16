#Reto: graficando la población de un país

from csv import reader
import matplotlib.pyplot as plt

with open('..\PHYTON\PLATZI\FUNCIONES Y MANEJO DE ERRORES\datas1.csv','r') as data:
    reader1 = reader(data)
    header = next(reader1)
    data1=[]
    for line in reader1:
        codict=dict()
        for i,j in zip(header,line):
            if 'Country' in i or 'World Population' in i :
                codict[i]=j
        data1.append(codict)


def graficar(data,name):
    data2 = sorted(data, key= lambda x: x['World Population Percentage'])
    labels=[i['Country'] for i in data2]
    values=[i['World Population Percentage'] for i in data2]
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.show()

graficar(data1,'Bolivia')



