multiples_list = []

for n in range(0, 1000):
    if n % 3 == 0 or n % 5 == 0:
        multiples_list.append(n)

print(multiples_list)
print(sum(multiples_list))