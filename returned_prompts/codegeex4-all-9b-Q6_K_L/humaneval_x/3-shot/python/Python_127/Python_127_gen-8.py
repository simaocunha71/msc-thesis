    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def intersection_length(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        return max(0, end - start)

    if intersection_length(interval1, interval2) == 0:
        return "NO"

    return "YES" if is_prime(intersection_length(interval1, interval2)) else "NO"

