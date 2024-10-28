def get_median(a, b):
    if len(a) == 0:
        return b[len(b) // 2]
    if len(b) == 0:
        return a[len(a) // 2]
    if len(a) > len(b):
        return get_median(b, a)
    if len(a) == 1:
        return (a[0] + b[len(b) // 2]) / 2.0