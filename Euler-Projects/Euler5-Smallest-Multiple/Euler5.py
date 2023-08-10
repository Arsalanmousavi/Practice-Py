# lcm(lcm(1,2),3)... - new a (lcm) is equal to previous lcm * i // gcd of them

import math

a = 1

for i in range(1, 21):
    a = a * i // math.gcd(a, i)

print(a)