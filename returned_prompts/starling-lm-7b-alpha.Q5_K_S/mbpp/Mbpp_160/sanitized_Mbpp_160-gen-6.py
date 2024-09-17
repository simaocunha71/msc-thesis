def find_solution(a, b, n):
    for x in range(n+1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None