
def intersection(interval1, interval2):
    if (interval1[1] < interval2[0]) or (interval1[0] > interval2[1]):
        return "NO"
    else:
        intersection_start = max(interval1[0], interval2[0])
        intersection_end = min(interval1[1], interval2[1])
        return "YES" if is_prime(intersection_end - intersection_start) else "NO"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
