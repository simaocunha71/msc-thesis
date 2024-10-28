    if interval1[0] <= interval2[1] and interval1[1] >= interval2[0]:
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start <= end and is_prime(end - start + 1):
            return "YES"
    return "NO"


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
