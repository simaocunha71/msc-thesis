def find_solution(a, b, n):
    if a == 0:
        if n % b == 0:
            return (0, n // b)
        else:
            return None