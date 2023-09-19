def sum_proper_divisors(n):
    divisors = [1]  # List to store the proper divisors
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def find_amicable_numbers(limit):
    amicable_numbers = []
    for num in range(2, limit):
        sum1 = sum_proper_divisors(num)
        sum2 = sum_proper_divisors(sum1)
        if num == sum2 and sum1 != sum2:
            amicable_numbers.append(num)
    return amicable_numbers

# Find amicable numbers under 10,000
limit = 10000
amicable_numbers = find_amicable_numbers(limit)

# Calculate the sum of amicable numbers
sum_of_amicable_numbers = sum(amicable_numbers)

# Print the result
print("Sum of amicable numbers:", sum_of_amicable_numbers)
