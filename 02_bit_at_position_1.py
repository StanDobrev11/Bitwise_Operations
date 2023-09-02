"""Write a program that prints the bit at position 1 of given integer.
We use the standard counting: from right to left, starting from 0."""

from numeric_system_converter import decimal_to_binary

number = int(input())

int_as_binary = decimal_to_binary(number)
print(int_as_binary[-2])
