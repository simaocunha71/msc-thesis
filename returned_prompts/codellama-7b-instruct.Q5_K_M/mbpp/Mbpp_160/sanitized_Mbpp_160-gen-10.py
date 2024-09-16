def find_solution(a, b, n):
    for x in range(n+1):
        if a*x + b > n:
            y = a*x + b - n
            return x, y
    return None