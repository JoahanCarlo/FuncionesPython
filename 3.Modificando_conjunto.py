#Modificando conjuntos
'''
    add(): Añade un elemento.
    update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
    discard(): Elimina un elemento y si ya existe no lanza ningún error.
    remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
    pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
    clear(): Elimina todo el contenido del conjunto.
'''
set_paises = {'col','mex','chi'}
size = len(set_paises)
print(size)

print('col' in set_paises)
print('pe' in set_paises)

#add
set_paises.add('pe')
print(set_paises)

#update
set_paises.update({'arg','par','pe'})
print(set_paises)

#remove
set_paises.remove('pe')
print(set_paises)


#dircard  --
#set_paises.discard('uk')
#print(set_paises)

#clear
set_paises.clear()
print(set_paises)
