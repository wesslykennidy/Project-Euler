A = [element**2 for element in range(1,101)]
K = sum(A)
#print (K)

result = 0
for i in range(1,101):
    result +=i
    B = result**2


print (B-K)