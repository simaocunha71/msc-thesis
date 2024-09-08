def find_solution(a, b, n):
    x, y = 0, 0
    while True:
        if a*x + b*y == n:
            return (x, y)
        x += 1
        y -= 1