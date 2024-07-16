#Dictionary Comprehension: condition

import random
countries = ['col','mex','bol','per']
popular2={country:random.randint(1,100)
          for country in countries}
print(popular2)  
result = {country: popular  for (country,popular) in popular2.items() if  popular>50}
print(result)

text = 'Hola, soy Joahan'
unico = {c: c.upper() for c in text  if c in 'aeiou'}
print(unico)

frase = 'Hola, soy Andres'
unico2 = {c: frase.count(c) for c in frase if c in 'aeiou'}
print(unico2)
unico3 = {}
