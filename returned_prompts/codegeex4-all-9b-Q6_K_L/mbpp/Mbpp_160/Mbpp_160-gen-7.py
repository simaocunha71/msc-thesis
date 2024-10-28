def find_solution(a, b, n):
    for x in range(n // a + 1):
        for y in range(n // b + 1):
            if a * x + b * y == n:
                return x, y
    return None

