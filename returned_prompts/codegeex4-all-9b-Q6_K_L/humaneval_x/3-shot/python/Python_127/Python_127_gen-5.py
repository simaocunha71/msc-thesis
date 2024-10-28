    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        """Determine the intersection of two intervals."""
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start <= end:
            return (start, end)
        else:
            return None

    def intersection_length(interval):
        """Calculate the length of an interval."""
        if interval is None:
            return 0
        else:
            return interval[1] - interval[0] + 1

    def is_prime_intersection(interval1, interval2):
        """Determine if the intersection of two intervals has a prime length."""
        intersection_ = intersection(interval1, interval2)
        if intersection_ is None:
            return "NO"
        else:
            length = intersection_length(intersection_)
            if is_prime(length):
                return "YES"
            else:
                return "NO"

    # Example usage:
    print(is_prime_intersection((1, 2), (2, 3)))  # Output: "NO"
    print(is_prime_intersection((-1, 1), (0, 4)))  # Output: "NO"
    print(is_prime_intersection((-3, -1), (-5, 5)))  # Output: "YES"

