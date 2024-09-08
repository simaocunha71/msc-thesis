def find_solution(a, b, n):
    if a*b == 0:
        return None
    x = n // b
    y = n // a
    while a*x + b*y != n:
        x -= 1
        y += 1
    return x, y