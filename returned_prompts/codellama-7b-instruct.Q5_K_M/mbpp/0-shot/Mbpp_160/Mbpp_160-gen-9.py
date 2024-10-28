def find_solution(a, b, n):
    for x in range(n+1):
        for y in range(n+1):
            if a*x + b*y == n:
                return x, y
    return None


