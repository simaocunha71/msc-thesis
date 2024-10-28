def find_solution(a, b, n):
    for x in range(abs(a) + abs(b) + 2):
        for y in range(abs(a) + abs(b) + 2):
            if a * x + b * y == n:
                return (x, y)
    return None