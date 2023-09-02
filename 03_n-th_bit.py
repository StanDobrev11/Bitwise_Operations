"""
Write a program that prints the bit at position n of given integer.
We use the standard counting: from right to left, starting from 0.
"""

from numeric_system_converter import decimal_to_binary

number = int(input())
position = int(input())

int_as_binary = decimal_to_binary(number)
if position > len(int_as_binary):
    zeros_to_add = position - len(int_as_binary)
    int_as_binary = '0' * (zeros_to_add + 1) + int_as_binary

int_as_binary = int_as_binary[::-1]
print(int_as_binary[position])
