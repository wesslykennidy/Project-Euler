multiplier = 1
n =100
for i in range (1, n+1):
    multiplier = multiplier * i

A = list(str(multiplier))
sum_element = 0
for k in A:
    sum_element +=int(k)
print(sum_element)
