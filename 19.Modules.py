#Modules

import sys
print(sys.path)

import re
text = 'Mi numero de telfono es 987645334 y el codigo del pais es +51, minuñmero de la suerte es 3'
result = re.findall('[0-9]+',text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result1 = time.asctime(local)
print(result1)
print(timestamp)

import collections
numbers = [1,1,1,2,2,2,3,3,3,4,5,5,5]
counter = collections.Counter(numbers)
print(counter)