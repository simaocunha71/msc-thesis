    def is_prime(number):
        if number < 2:
            return False
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
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


