def find_solution(a, b, n):
    if b == 0:
        if a == 0:
            return None
        return 0, n//a
    x = 0
    y = n
    while b > 0:
        q = a//b
        a, b = b, a-q*b
        x, y = y, x-q*y
    if a > 0:
        return None
    return x, y
    # return (x, y) if a == 0 else None
    # return (x, y) if a % b == 0 else None
    # return (x, y)
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y)
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y) if a % b == 0 else None
    # return None
    # return (x, y