
def is_prime(n):
    """Function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Function to determine whether the length of intersection of two intervals is a prime number"""
    # Find intersection of intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    # If intervals do not intersect
    if start > end:
        return "NO"
    # If intersection is a prime number
    if is_prime(end - start + 1):
        return "YES"
    else:
        return "NO"

print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"

def test_intersection():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 3), (2, 4)) == "NO"
    assert intersection((1, 1), (1, 2)) == "YES"
    assert intersection((1, 2), (2, 2)) == "NO"
    assert intersection((1, 2), (1, 1)) == "NO"
    assert intersection((1, 1), (1, 1)) == "NO"
    assert intersection((1, 3), (2, 3)) == "NO"
    assert intersection((1, 3), (2, 4)) == "NO"
    assert intersection((1, 3), (1, 4)) == "YES"
    assert intersection((1, 3), (3