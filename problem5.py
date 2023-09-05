from math import gcd, lcm

result = 1
for i in range(1, 21):
    result = lcm(result, i)

print(result)
