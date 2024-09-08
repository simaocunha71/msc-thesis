def next_power_of_2(n):
    if n <= 0:
        return 1
    p = 1
    while p < n:
        p *= 2
    return p

print(next_power_of_2(0))

