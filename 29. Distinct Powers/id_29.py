A = list()
for a in range (2,101):
    for b in range (2,101):
        product = b**a
        A.append(product)

output = list()
for element in A:
    if element not in output:
        output.append(element)
print (len(output))