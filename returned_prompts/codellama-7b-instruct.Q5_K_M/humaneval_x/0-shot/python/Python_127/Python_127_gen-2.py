
def intersection(interval1, interval2):
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"
    else:
        return "YES" if len(set(range(max(interval1[0], interval2[0]), min(interval1[1], interval2[1]) + 1))) == 1 else "NO"
