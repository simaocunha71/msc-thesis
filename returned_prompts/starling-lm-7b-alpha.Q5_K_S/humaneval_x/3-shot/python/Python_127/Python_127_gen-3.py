    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if end < start:
            return []
        else:
            return [start, end]

    if len(intersection(interval1, interval2)) == 0:
        return "NO"

    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if end < start:
        return []
    else:
        return [start, end]


def is_prime_length(intersection):
    length = intersection[1] - intersection[0] + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"


