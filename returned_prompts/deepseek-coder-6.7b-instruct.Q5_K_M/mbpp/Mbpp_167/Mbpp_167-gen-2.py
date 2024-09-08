def next_power_of_2(n):
    if n < 0:
        return 0
    p = 1
    while p < n:
        p *= 2
    return p

print(next_power_of_2(0))  # returns 1

