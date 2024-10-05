    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
            return "NO"
        else:
            start = max(interval1[0], interval2[0])
            end = min(interval1[1], interval2[1])
            length = end - start + 1
            if is_prime(length):
                return "YES"
            else:
                return "NO"


