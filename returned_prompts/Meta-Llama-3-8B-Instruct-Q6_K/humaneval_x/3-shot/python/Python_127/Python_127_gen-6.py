    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    interval1_start, interval1_end = interval1
    interval2_start, interval2_end = interval2

    intersection_start = max(interval1_start, interval2_start)
    intersection_end = min(interval1_end, interval2_end)

    if intersection_start > intersection_end:
        return "NO"

    intersection_length = intersection_end - intersection_start
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"


