num = int(input())
pos = int(input())

mask = pos << pos
print(f"{mask:b}")

result = num ^ mask
print(bin(num))
print(bin(result))
