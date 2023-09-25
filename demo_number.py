# числа

from decimal import Decimal

a = 123
a = a + 456
a = a - 456
a = a / 456
a = a * 456
a = a ** 3
a = (100 + 200) / 300 * 400

a = 123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789

a = 0b1100010010
a = 0o1234567
a = 0x123456df

a = 0.5

print(a)

a = 0.1 + 0.2
print(a)
# assert a == 0.3


# math

import math
print(math.pi)


# random

import random

random.seed("some word")

print("-------")

print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

print("-------")

print(round(1.3333, 2))
