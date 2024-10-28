    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Find the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # Check if the intersection has a prime length
    if is_prime(end - start):
        return "YES"
    else:
        return "NO"

