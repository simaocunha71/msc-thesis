    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def length(interval):
        return interval[1] - interval[0] + 1

    if not (interval1[0] <= interval1[1] and interval2[0] <= interval2[1]):
        return "NO"
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"

    intersection_length = length((max(interval1[0], interval2[0]), min(interval1[1], interval2[1])))

    return "YES" if is_prime(intersection_length) else "NO"


