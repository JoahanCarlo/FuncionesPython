#Dictionary Comprehension
'''
dict = {}
for i in range(1,5):
    dict[i] = i*2
print(dict)

dict_2 = {i:i*2 for i in range(1,6)}
print(dict_2)

import random
countries = ['col','mex','bol','per']
popular = {}
for country in countries:
    popular[country] = random.randint(1,100)
print(popular)

popular2={country:random.randint(1,100)
          for country in countries}
print(popular2)
'''
nombres = ['nicol','zule','santi']
age = [23,45,12]

print(list(zip(nombres,age)))

new_dict = {name:age for (name,age) in zip(nombres,age)}
print(new_dict)

new_dict2 = {nombres[i]:age[i] for i in range(len(nombres))}
print(new_dict2)
