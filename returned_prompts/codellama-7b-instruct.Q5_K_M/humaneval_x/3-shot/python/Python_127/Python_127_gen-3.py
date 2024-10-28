    if interval1[0] > interval1[1] or interval2[0] > interval2[1]:
        return "NO"
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"
    else:
        return "YES"


