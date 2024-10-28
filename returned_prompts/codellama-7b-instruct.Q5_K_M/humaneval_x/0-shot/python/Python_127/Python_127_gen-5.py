
def intersection(interval1, interval2):
    # check the intersection of the two intervals
    # if the intersection doesn't exist, return "NO"
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"
    # get the intersection of the two intervals
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])
    # check if the length of the intersection is a prime number
    if len(range(intersection_start, intersection_end + 1)) == 1:
        return "YES"
    else:
        return "NO"

B:

def intersection(interval1, interval2):
    if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
        return "NO"
    
    return "YES" if len(set(range(max(interval1[0], interval2[0]), min(interval1[1], interval2[1]) + 1)) - set([interval1[1], interval2[1]])) == 1 else "NO"
