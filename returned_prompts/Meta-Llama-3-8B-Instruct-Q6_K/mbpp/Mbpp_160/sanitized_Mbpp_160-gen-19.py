def find_solution(a, b, n):
    for x in range(-abs(b), abs(a) + 1):
        for y in range(-abs(a), abs(b) + 1):
            if a * x + b * y == n:
                return (x, y)
    return None