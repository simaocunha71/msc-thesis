    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def interval_length(start, end):
        return end - start + 1

    if not interval1[0] <= interval1[1] or not interval2[0] <= interval2[1]:
        return "NO"

    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"

    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])

    intersection_length = interval_length(intersection_start, intersection_end)

    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"



