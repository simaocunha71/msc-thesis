
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    s = max(interval1[0], interval2[0])
    e = min(interval1[1], interval2[1])
    if e < s:
        return "NO"
    if is_prime(e - s + 1):
        return "YES"
    return "NO"


def intersection(interval1, interval2):
    # Your code here
    if interval1[1] < interval2[0]:
        return "NO"
    if interval2[1] < interval1[0]:
        return "NO"

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if end < start:
        return "NO"
    if is_prime(end - start + 1):
        return "YES"
    return "NO"


def intersection(interval1, interval2):
    # Your code here
    if interval1[1] < interval2[0]:
        return "NO"
    if interval2[1] < interval1[0]:
        return "NO"

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if end < start:
        return "NO"
    if is_prime(end - start + 1):
        return "YES"
    return "NO"








































































































