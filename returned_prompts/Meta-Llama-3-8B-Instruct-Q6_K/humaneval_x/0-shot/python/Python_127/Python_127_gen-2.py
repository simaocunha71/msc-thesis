def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start > intersection_end:
        return "NO"
    intersection_length = intersection_end - intersection_start + 1
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
# test cases
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"
print(intersection((1, 3), (2, 4)))  # "NO"
print(intersection((0, 4), (1, 3)))  # "NO"  # "NO"
print(intersection((-1, 0), (0, 1)))  # "YES"
print(intersection((0, 1), (1, 2)))  # "NO"
print(intersection((1, 2), (2, 2)))  # "NO"
print(intersection((-1, 2), (-2, 2)))  # "YES"  # "YES"
print(intersection((0, 3), (1, 3)))  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "NO"  # "