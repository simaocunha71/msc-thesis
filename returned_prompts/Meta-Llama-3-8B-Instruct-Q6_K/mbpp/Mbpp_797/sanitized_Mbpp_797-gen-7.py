def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)  # or sum([i for i in range(l, r+1) if i % 2 != 0]) in python 3.9 and above