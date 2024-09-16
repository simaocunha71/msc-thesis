def find_solution(a, b, n):
    for x in range(n + 1):
        y = (n - x) // a
        if y * b == (n - x):
            return (x, y)
    return None