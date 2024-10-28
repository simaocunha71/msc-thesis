def find_solution(a, b, n):
    if a * b == 0:
        return None
    x = n // b
    y = n % b
    if x * b + y * a == n:
        return (x, y)
    return None