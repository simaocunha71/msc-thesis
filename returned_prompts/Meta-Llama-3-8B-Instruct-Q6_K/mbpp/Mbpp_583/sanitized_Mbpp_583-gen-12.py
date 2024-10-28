import math
def catalan_number(n):
    result = 1
    for i in range(1, n+1):
        result = result * (2*n - i + 1) // i
    return result // (n+1)