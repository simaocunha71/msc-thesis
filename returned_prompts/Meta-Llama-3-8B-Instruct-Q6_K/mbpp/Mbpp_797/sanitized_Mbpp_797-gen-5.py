def sum_in_range(l, r):
    return sum(i for i in range(l,r+1) if i % 2 != 0)  # or sum(range(l+1,r+2,2)) for a more concise version