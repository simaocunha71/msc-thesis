    if not interval1[0] <= interval1[1] or not interval2[0] <= interval2[1]:
        return "NO"

    if not interval1[0] <= interval2[1] and interval2[0] <= interval1[1]:
        return "NO"

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return "NO"

    return "YES" if is_prime(end - start + 1) else "NO"


def is_prime(n: int) -> bool:
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


