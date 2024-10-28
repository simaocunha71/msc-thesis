
def find_solution(a, b, n):
    if a == 0:
        if b == 0:
            return None
        else:
            return (n % b, -(n // b))
    else:
        x = find_solution(b, a % b, a // b)
        return (x[1], x[0] - a * x[1]) if x else None


