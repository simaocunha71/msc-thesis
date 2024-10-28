
def is_prime(n):
    """
    Helper function to determine if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """
    Main function to determine if the intersection length is prime.
    """
    # If the intervals don't intersect, return immediately
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"

    # Calculate the intersection
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    length = end - start + 1

    # If the length is prime, return "YES"
    if is_prime(length):
        return "YES"

    return "NO"

# Test cases
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"


































































































































































































