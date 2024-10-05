
    def is_prime(n):
        """Check if a number is a prime number"""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def intersection(interval1, interval2):
        """Find intersection of two intervals"""
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        return "YES" if is_prime(length) else "NO"

