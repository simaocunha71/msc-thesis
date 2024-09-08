def highest_Power_of_2(n):
    i = 0
    while 2 ** i <= n:
        i += 1
    return 2 ** (i - 1)

print(highest_Power_of_2(10))  # 8


