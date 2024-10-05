
    def is_prime(n):
        """Helper function to check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        """Find the intersection of two intervals and check if its length is a prime number"""
        # find the intersection
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:  # if the intervals don't intersect
            return "NO"

        # check if the length of the intersection is a prime number
        length = end - start + 1
        return "YES" if is_prime(length) else "NO"





# Test Cases:

print(intersection((1, 2), (2, 3)))  #  NO
print(intersection((-1, 1), (0, 4)))  # NO
print(intersection((-3, -1), (-5, 5)))  # YES
print(intersection((1, 5), (3, 7)))  # YES
print(intersection((1, 3), (2, 4)))  # NO
print(intersection((1, 3), (1, 3)))  # YES
print(intersection((1, 2), (2, 5)))  # NO
print(intersection((5, 7), (6, 8)))  # NO
print(intersection((6, 8), (7, 9)))  # YES
print(intersection((1, 5), (2, 4)))  # NO
print(intersection((1, 5), (4, 6)))  # YES
print(intersection((-1, 1), (-1, 1)))  # YES
print(intersection((-1, 1), (0, 0)))  # NO
print(intersection((-1, 1), (-2, -1)))  # NO
print(inter