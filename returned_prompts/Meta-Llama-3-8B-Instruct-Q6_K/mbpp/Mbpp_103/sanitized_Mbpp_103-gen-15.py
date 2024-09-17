import math
def eulerian_num(n, m):
    result = math.factorial(n-1) // math.factorial(m-1)
    for i in range(m, n):
        result *= i
    return result