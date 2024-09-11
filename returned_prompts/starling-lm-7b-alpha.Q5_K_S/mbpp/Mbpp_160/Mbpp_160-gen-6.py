def find_solution(a, b, n):
    for x in range(n+1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None

find_solution(2, 3, 7) # (2, 1)

"""
def find_solution(a, b, n):
    for x in range(n+1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None
"""

"""
def find_solution(a, b, n):
    if n % b == 0:
        return (n // b, 0)
    for x in range(n+1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None
"""

"""
def find_solution(a, b, n):
    for x in range(n + 1):
        if n % b == (a * x) % b:
            return (x, (n - (a * x)) // b)
    return None
"""

"""
def find_solution(a, b, n):
    for x in range(n+1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None
"""

"""
def find_solution(a, b, n):
    for x in range(n+1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None
"""

"""
def find_solution(a, b, n):
    for x in range(n + 1):
        if (n - (a * x)) % b == 0:
            return (x, (n - (a * x)) // b)
    return None
"""

"""
def find