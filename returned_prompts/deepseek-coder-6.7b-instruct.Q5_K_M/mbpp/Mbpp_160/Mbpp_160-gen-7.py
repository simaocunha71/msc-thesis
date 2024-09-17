
def find_solution(a, b, n):
    results = None
    for x in range(n+1):
        for y in range(n+1):
            if a*x + b*y == n:
                results = (x, y)
                return results
    return results

