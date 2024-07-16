#Operaciones con conjuntos

set_a={'col','mex','bol'}
set_b={'pe','bol'}

#Unión de conjuntos
set_union = set_a.union(set_b)
print(set_union)
print(set_a | set_b)

#Intersección de conjuntos
set_interseccion = set_a.intersection(set_b)
print(set_interseccion)
print(set_a & set_b)

#Diferencia de conjuntos
set_diferencia = set_a.difference(set_b)
print(set_diferencia)
print(set_a - set_b)
print(set_b.difference(set_a))
print(set_b-set_a)

#Diferencia simetrica
set_simetrica = set_a.symmetric_difference(set_b)
print(set_simetrica)
print(set_a ^ set_b)