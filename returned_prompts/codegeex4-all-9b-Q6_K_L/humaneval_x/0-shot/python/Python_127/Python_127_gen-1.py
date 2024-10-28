def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_intersection_length(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        return max(0, end - start)

    intersection_length = get_intersection_length(interval1, interval2)
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

print(intersection((-3, -1), (-5, 5)))