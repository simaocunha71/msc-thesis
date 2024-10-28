
def intersection(interval1, interval2):
    """
    (start1, end1)
    (start2, end2)
    """
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"
    else:
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        return "YES" if end - start + 1 == 2 else "NO"

