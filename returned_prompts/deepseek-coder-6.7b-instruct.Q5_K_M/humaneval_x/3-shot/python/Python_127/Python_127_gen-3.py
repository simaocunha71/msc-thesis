    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end:
        return "NO"
    return "YES" if is_prime(end - start + 1) else "NO"


