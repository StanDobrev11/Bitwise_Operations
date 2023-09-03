"""You are given an array of positive integers in a single line, separated by a space (' ').
All numbers occur even number of times except one number which occurs odd number of times.
Find it, using only bitwise operations."""

num_list = [int(x) for x in input().split()]
count = 0
for idx in range(len(num_list)):
    current_num = num_list[idx]
    pair_count = 0
    for next_idx in range(idx + 1, len(num_list)):
        next_num = num_list[next_idx]
        if current_num ^ next_num != 0:
            continue
        else:
            pair_count += 1
    if pair_count > 0 and pair_count % 2 == 0:
        print(current_num)
