largest_palindrome = 0

for number1 in range(999, 99, -1):
    for number2 in range(number1, 99, -1):
        multiple = number1 * number2

        if multiple <= largest_palindrome:
            break

        digits = []
        while multiple > 0:
            digits.append(multiple % 10)
            multiple = multiple // 10

        if digits == digits[::-1]:
            largest_palindrome = (number1 * number2)

print(largest_palindrome)