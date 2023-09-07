numbers = []

answer = []

for i in range(100, 1000):
    numbers.append(str(i))

for num in numbers:

    if "0" in num:
        continue
    else:
        if len(set(num)) == 2:
            answer.append(num)

print(answer)
print(len(answer))
