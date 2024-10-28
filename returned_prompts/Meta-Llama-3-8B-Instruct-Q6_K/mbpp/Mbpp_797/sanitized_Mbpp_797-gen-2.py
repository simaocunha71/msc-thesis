def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)  # sum of odd numbers in the range l to r