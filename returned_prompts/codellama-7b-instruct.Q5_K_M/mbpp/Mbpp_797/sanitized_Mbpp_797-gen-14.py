def sum_in_range(l, r):
    sum = 0
    for i in range(l, r+1, 2):
        sum += i
    return sum