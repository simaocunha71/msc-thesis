def get_median(l1, l2, n):
    l1.extend(l2)
    l1.sort()
    median = l1[n//2]
    if n % 2 == 0:
        median = (median + l1[n//2 - 1]) / 2
    return median