"""You are given a positive integer number and one binary digit B (0 or 1).
Your task is to write a program that finds the number of binary digits (B) in given integer."""

from numeric_system_converter import decimal_to_binary

integer = int(input())
num_to_count = input()

int_as_binary = decimal_to_binary(integer)

print(int_as_binary.count(num_to_count))
