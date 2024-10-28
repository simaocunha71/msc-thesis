def find_solution(a, b, n):
    for x in range(n+1):
        if a*x >= n:
            y = a*x - n
            if b*y >= 1:
                return (x, y)
    return None