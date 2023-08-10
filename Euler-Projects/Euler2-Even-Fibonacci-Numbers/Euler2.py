fibonacci = []

current, next_number = 1, 1

while next_number < 4e6:
    if next_number % 2 == 0:
        fibonacci.append(next_number)
    current, next_number = next_number, current + next_number

print(fibonacci)
print(sum(fibonacci))
