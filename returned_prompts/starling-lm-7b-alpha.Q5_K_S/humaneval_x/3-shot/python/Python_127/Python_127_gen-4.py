    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        start, end = interval1
        start2, end2 = interval2
        if end < start or end2 < start2:
            return "NO"
        return "YES" if is_prime(max(end, end2) - min(start, start2)) else "NO"


