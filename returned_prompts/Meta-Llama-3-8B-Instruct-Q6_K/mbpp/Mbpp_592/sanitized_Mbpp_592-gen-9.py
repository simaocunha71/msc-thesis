import math
def sum_Of_product(n):
    sum = 0
    for i in range(n+1):
        for j in range(i+1):
            sum += comb(n, j)
    return sum
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k)) if k <= n else 0