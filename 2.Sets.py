#Sets

'''
    Se pueden modificar
    No tienen un orden
    No pueden tener elementos duplicados
'''

set_paises ={'col','mex','bol'}
print(set_paises)
print(type(set_paises))

set_numbers = {2,3,4,5,6,7}
print(set_numbers)

set_string =set('hoola')
print(set_string)

set_from_tuples = set(('a','b','c'))
print(set_from_tuples)
print(type(('a','b','c')))

numbers = [1,2,3,4,5,6,6,7,7,1]
set_numbers1=set(numbers)
print(set_numbers1)
unique_numbers = list(set_numbers1)
print(unique_numbers)