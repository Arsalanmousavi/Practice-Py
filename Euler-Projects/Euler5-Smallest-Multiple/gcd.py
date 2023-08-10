# GCD of a and b
a = 54
b = 21

# check non-zero b
if b == 0:
    print("Division by", b)

else:
    while a % b != 0:  # euclidean algorithm
        a, b = b, a % b
        print(a, b)
    print("GCD:", b)