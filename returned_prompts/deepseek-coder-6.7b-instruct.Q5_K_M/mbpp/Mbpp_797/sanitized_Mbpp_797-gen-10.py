def sum_in_range(l,r):
    sum_odd = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            sum_odd += i
    return sum_odd