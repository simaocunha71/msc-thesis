
def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if end >= start:
        return "NO"
    if (end-start) % 2 == 0 and (end-start) != 0:
        return "NO"
    else:
        return "YES"
