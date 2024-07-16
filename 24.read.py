#Leer un CSV

import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        header = next(reader)
        print(header)
        
if __name__ == '__main__':
    read_csv('./PLATZI/FUNCIONES Y MANEJO DE ERRORES/datas.csv')
        
def read_csv1(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        header = next(reader)
        for row in reader:
            iterable = zip(header,row)
            print(list(iterable))

if __name__ == '__main__':
    read_csv('./PLATZI/FUNCIONES Y MANEJO DE ERRORES/datas.csv')
    
    
