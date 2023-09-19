def largest_prime_number (n):
    largest_number = -1
    i = 2
    while i*i <= n:
        while n%i == 0:
            largest_number = i
            n = n // i
        i = i+1
    if n > 1:
        largest_number = n
    return largest_number

ng = 600851475143
product = largest_prime_number(ng)
print (product)
