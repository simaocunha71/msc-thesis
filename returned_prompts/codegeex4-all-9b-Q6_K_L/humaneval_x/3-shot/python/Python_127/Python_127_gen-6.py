    def is_prime(n):
        """Return True if n is a prime number, False otherwise."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    intersection_length = min(interval1[1], interval2[1]) - max(interval1[0], interval2[0])
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

