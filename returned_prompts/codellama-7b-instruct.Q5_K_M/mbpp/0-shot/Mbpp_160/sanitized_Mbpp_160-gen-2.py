def find_solution(a, b, n):
    for x in range(n+1):
        y = (n-x)//a
        if y*a+y*b == n:
            return x, y
    return None