    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > end2 or end1 < start2:
        return "NO"

    return "YES" if len(set(range(max(start1, start2), min(end1, end2)))) > 1 else "NO"


