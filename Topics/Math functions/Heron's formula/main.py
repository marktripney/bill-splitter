import math

# Gather input
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2

area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(area)