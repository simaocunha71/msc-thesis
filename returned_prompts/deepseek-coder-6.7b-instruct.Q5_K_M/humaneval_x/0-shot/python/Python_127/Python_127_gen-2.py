
    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        if length < 2: return "NO"
        for i in range(2, int(length**0.5)+1):
            if length % i == 0:
                return "NO"
        return "YES"


    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        if is_prime(length):
            return "YES"
        else:
            return "NO"


    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        if length < 2: return "NO"
        if length == 2: return "YES"
        if length % 2 == 0: return "NO"
        for i in range(3, int(length**0.5)+1, 2):
            if length % i == 0:
                return "NO"
        return "YES"


    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        if length < 2: return "NO"
        if length in [2, 3]: return "YES"
