#El scope

price=100  #Alcance global
def increment():
    price= price +50
    print(price)
    return price

print(price)
price2 = increment()
print(price2)
