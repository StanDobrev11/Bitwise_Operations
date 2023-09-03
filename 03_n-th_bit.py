"""
Write a program that prints the bit at position n of given integer.
We use the standard counting: from right to left, starting from 0.
"""

number = int(input())
position = int(input())

mask = number >> position
print(mask & 1)
