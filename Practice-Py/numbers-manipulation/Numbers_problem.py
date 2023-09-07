numbers = []

answer = []

for i in range(100, 1000):
    numbers.append(str(i))

for num in numbers:

    if "0" in num:
        continue
    else:
        temp = []
        for digit in num[0:]:
            if digit not in temp:
                temp.append(digit)
        if len(temp) == 2:
            answer.append(num)

print(answer)
print(len(answer))
