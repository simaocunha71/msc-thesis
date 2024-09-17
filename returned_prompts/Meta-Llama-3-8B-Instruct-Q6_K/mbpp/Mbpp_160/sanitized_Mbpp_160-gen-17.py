def find_solution(a, b, n):
    for x in range(-10000, 10001):
        for y in range(-10000, 10001):
            if a * x + b * y == n:
                return (x, y)
    return None