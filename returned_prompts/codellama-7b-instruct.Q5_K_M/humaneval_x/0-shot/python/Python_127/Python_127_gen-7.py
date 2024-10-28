
def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start <= end:
        return "NO"
    else:
        return "YES" if len(set(range(start, end + 1))) == 1 else "NO"
