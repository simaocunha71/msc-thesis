def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if a == 0:
        if b == n:
            return 0, 1
        else:
            return None
    if b == 0:
        if a == n:
            return 1, 0
        else:
            return None
    if n % a == 0:
        x = n // a
        y = 0
    elif n % b == 0:
        x = 0
        y = n // b
    else:
        gcd, x1, x2 = extended_euclidean(a, n)
        y1 = -n // b * x2
        y = y1
        x = x2
    return x, y
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x
    return 0, 0, 0  # Default return value if base case is not met. This line should be removed.