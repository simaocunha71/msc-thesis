
def is_prime(n):
    """
    Determine whether the given number is prime
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """
    Intersection of two intervals
    """
    s1, e1 = interval1
    s2, e2 = interval2
    if s1 > e1:
        s1, e1 = e1, s1
    if s2 > e2:
        s2, e2 = e2, s2
    if s2 > e1:
        return "NO"
    if s1 > e2:
        return "NO"
    return "YES" if is_prime(e2 - s1 + 1) else "NO"


# Intersection of two intervals (start, end)
# The given intervals are closed which means that the interval (start, end)
# includes both start and end. For each given interval, it is assumed that its start is less or equal its end.
# Your task is to determine whether the length of intersection of these two intervals is a prime number.
# Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
# which its length is 1, which is not a prime number.
# If the length of the intersection is a prime number, return "YES",
# otherwise, return "NO".
# If the two intervals don't intersect, return "NO".


# You are given two intervals, where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
# The given intervals are closed which means that the interval (start, end) includes both start and end.
# Your task is to determine whether the length of intersection of these two intervals is a prime number.
# Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
# which its length is 1, which not a prime number.
# If the length of the intersection is a prime number, return "Y