
def find_solution(a, b, n):
    for y in range(n+1):
        x = (n - b*y) / a
        if x.is_integer() and 0 <= x <= n:
            return (int(x), y)
    return None


