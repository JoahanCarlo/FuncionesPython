#Mis propios módulos

def get_population():
    keys = ['col','bol']
    values = [300,400]
    return keys, values 

A='Hola'

def population_by_country(data,country):
    result1 = list(filter(lambda item: item['Country']==country,data))
    return result1

