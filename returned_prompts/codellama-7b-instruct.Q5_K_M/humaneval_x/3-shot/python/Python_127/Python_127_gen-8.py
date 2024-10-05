    start1, end1 = interval1
    start2, end2 = interval2

    if start1 <= start2:
        start = start2
    else:
        start = start1

    if end1 <= end2:
        end = end1
    else:
        end = end2

    if start <= end:
        return "YES"
    else:
        return "NO"


