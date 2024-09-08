def find_solution(a, b, n):
    for x in range(n):
        for y in range(n):
            if a * x + b * y == n:
                return (x, y)
    return None