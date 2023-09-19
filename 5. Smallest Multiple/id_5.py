import math as m
result = 1
for i in range (1,11):
    result *= i // m.gcd (result, i)
print (result)

