"""You are given an array of positive integers in a single line, separated by a space (' ').
All numbers occur even number of times except one number which occurs odd number of times.
Find it, using only bitwise operations."""


def xor(a, b):
    return (a and not b) or (not a and b)


# num_list = [int(x) for x in input().split()]
#
# for idx in range(len(num_list)):
#     result = 0
#     current_num = num_list[idx]
#     for next_idx in range(idx + 1, len(num_list)):
#         next_num = num_list[next_idx]
#         result = xor(current_num, next_num)
#         print(result)

a = "1001 1100"
b = "0011 0100"

print(bool(a) != bool(a))