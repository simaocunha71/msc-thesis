def sum_in_range(l, r):
    return sum(range(l, r+1, 2)) if l % 2 != 0 else sum(range(l+1, r+1, 2))  # 1 is odd, so l+1 if l is even