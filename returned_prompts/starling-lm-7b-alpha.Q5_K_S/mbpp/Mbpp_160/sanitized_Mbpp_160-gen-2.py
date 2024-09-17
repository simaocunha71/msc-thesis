def find_solution(a, b, n):
    if abs(a) > abs(b):
        a, b = b, a
        n, a, b = a, b, n
    if a == 0:
        if b == 0:
            return None
        else:
            return (n % b, n)
    else:
        x = n % b
        y = (n - a * x) // b
        return (x, y)