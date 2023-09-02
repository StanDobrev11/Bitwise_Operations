"""
Write a program that sets the bit at position n to 0. Print the resulting integer.
"""

from numeric_system_converter import decimal_to_binary, binary_to_decimal

number = int(input())
position = int(input())

int_as_binary = decimal_to_binary(number)

position = len(int_as_binary) - position - 1

int_as_binary = int_as_binary[:position] + '0' + int_as_binary[position + 1:]
decimal = binary_to_decimal(int_as_binary)
print(decimal)
