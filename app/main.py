

import utils

keys, values = utils.get_population()
print(keys,values)

print(utils.A)

data = [
    {
    'Country': 'Colombia',
    'Population': 300 
},
       {
    'Country': 'Chile',
    'Population': 200 
}
    ]

result1= utils.population_by_country(data,'Colombia')
print(utils.A)

country = input('Type Country => ')