"""
Write a program that sets the bit at position n to 0 or 1. Print the resulting integer.
n = n & ~(1 << p) | (b << p) where b is a bit in range 0 - 1.
"""

number = int(input())
position = int(input())
bit_to = int(input())

print(f"{number:b}")
mask_1 = ~(1 << position)
print(f"{mask_1:b}")
mask_2 = (bit_to << position)
print(f"{mask_2:b}")

n = number & mask_1 | mask_2
print(f"{n:b}")
print(n)

