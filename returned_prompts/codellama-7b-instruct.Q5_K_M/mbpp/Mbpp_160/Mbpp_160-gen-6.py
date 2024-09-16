def find_solution(a, b, n):
    x, y = None, None
    if a == 0:
        x = n
    else:
        x = n // b
        y = n - a * x
    return x, y

