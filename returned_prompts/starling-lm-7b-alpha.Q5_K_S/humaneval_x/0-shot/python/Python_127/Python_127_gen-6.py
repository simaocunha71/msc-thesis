
def intersection(interval1, interval2):
    # Check whether the two intervals intersect
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    # Compute the intersection of the two intervals
    left = max(interval1[0], interval2[0])
    right = min(interval1[1], interval2[1])
    # Compute the length of the intersection
    length = right - left + 1
    # Check whether the length of the intersection is a prime number
    if length == 1:
        return "YES"
    for i in range(2, length):
        if length % i == 0:
            break
    else:
        return "YES"
    # Return "NO" if the length is not a prime number
    return "NO"

# Test the function
print(intersection((-3, -1), (-5, 5)))





# Python program to check whether a number is prime or not
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def intersection(interval1, interval2):
    # Check whether the two intervals intersect
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    # Compute the intersection of the two intervals
    left = max(interval1[0], interval2[0])
    right = min(interval1[1], interval2[1])
    # Compute the length of the intersection
    length = right - left + 1
    # Check whether the length of the intersection is a prime number
    if isPrime(length):
        return "YES"
    # Return