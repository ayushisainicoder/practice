num = 12456789
reverse_num = 0
while num!=0:
    last_num = num % 10
    reverse_num = reverse_num * 10 + last_num
    num = num // 10
print(reverse_num)