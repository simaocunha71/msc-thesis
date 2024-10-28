    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return "NO"
        else:
            return "YES" if is_prime(interval2[1] - interval1[0]) else "NO"


