def find_solution(a, b, n):
    for x in range(-1000, 1001):
        for y in range(-1000, 1001):
            if a * x + b * y == n:
                return (x, y)
    return None