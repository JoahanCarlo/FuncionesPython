#Lambdas
#Funciones Anónimas o lambdas, 
# en donde no tienen un identificador o no tienen un nombre, 
# se puede definir su estructura de la siguiente manera: lambda argumentos: 
# expresión, las funciones lambda pueden tener 
# los argumentos que se requieran pero solo una linea de código o una expresión.

def increment(x):
    return x+1

increment_v2 = lambda x : x+1

result = increment(10)
print(11)

result = increment_v2(20)
print(result)

full_name = lambda name,last_name: f'Mi nombre es  {name} y mis apellidos son {last_name}'
text = full_name('Joahan Carlo','Nuñez Soto')
print(text)