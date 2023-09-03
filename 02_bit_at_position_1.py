"""Write a program that prints the bit at position 1 of given integer.
We use the standard counting: from right to left, starting from 0."""

number = int(input())

bit_psn_0 = number >> 1
print(bit_psn_0 & 1)
