def find_solution(a, b, n):
    if a == 0 and b == 0 and n != 0:
        return None
    if b == 0:
        return (n / a, 0)
    if a == 0:
        return (0, n / b)
    x = n / a
    y = (n - a * x) / b
    return (x, y)