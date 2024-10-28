import math
def math_comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
def eulerian_num(n, m):
    result = 0
    for k in range(n+1):
        if k % 2 == 0:
            result += math_comb(n-k, m)
        else:
            result -= math_comb(n-k, m)
    return result