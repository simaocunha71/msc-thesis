def find_solution(a, b, n):
    if (n % a) == 0:
        return (n//a, 0)
    elif (n % b) == 0:
        return (0, n//b)
    else:
        return None