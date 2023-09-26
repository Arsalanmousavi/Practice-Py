prime_factors = []
number = int(input("Give me a number so I can give you its prime factors: "))

for factor in range(2, number + 1):
    while number % factor == 0:
        number //= factor
        prime_factors.append(factor)
    if number == 1:
        break

max_prime_factor = max(prime_factors)

print(prime_factors)
print(max_prime_factor)
