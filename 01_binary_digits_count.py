from numeric_system_converter import decimal_to_binary

integer = int(input())
num_to_count = input()

int_as_binary = decimal_to_binary(integer)

print(int_as_binary.count(num_to_count))
