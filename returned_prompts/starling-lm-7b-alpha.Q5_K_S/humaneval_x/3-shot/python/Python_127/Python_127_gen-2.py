    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        start, end = min(interval1[0], interval2[0]), max(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        if is_prime(length):
            return "YES"
        return "NO"


