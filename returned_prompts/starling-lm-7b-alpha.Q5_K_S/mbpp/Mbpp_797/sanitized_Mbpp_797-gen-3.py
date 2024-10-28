def sum_in_range(l, r):
    total = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            total += i
    return total