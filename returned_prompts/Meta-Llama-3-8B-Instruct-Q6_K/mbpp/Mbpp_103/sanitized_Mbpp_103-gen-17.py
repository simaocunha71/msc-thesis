import math
def eulerian_num(n, m):
    if m > n - 1:
        return 0
    else:
        return sum((-1)**i * (math.factorial(n-1) // (math.factorial(i) * math.factorial(n-1-i))) for i in range(m+1))