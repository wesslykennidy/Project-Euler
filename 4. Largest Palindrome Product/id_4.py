def palindrome_verify(n):
    return str(n) == str(n)[::-1]

upper_limit = 1000
lower_limit = 100
max_number = 0
for i in range (100,1000):
    for j in range(100,1000):
        product = i*j
        if palindrome_verify(product) and product > max_number:
            max_number = product

print (max_number)

