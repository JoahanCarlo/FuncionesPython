#Higher order function: una función dentro de otra función


def increment (x):
    return x +1

increment_v2 = lambda x: x + 1

def high_function(x,func):
    return x + func(x)

high_function_v2 = lambda x, func: x + func(x)

result = high_function(2,increment)
print(result)

result = high_function_v2(2, increment_v2)
print(result)
result = high_function_v2(2, lambda x: x * 5)
print(result)
result = high_function_v2(2, lambda x: x + 3)
print(result)