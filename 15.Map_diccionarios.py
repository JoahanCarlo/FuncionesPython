#Map con diccionarios

items = [
    {
        'productos':'camisa',
        'precio': 100
    },
    {
        'producto':'pantalon',
        'precio':300
    },
    {
        'procuto':'camisa',
        'precio' : 280
    }
]

prices = list(map(lambda item: item['precio'],items))
print(prices)

def agreg_imp(item):
    item['taxes'] = item['precio']*.19
    return item

new_items = list(map(agreg_imp,items))
print(new_items)