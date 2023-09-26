# GCD of a and b
a = int(input("Give me the first number:"))
b = int(input("Give me the second number:"))

# check non-zero b
if b == 0:
    print("Division by", b)

else:
    while a % b != 0:  # euclidean algorithm
        a, b = b, a % b
        print(a, b)
    print("GCD:", b)
