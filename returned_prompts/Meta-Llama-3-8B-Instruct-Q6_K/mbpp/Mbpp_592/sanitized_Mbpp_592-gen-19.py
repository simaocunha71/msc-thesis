import math
def sum_Of_product(n):
    sum = 0
    for i in range(n):
        for j in range(i+1, n+1):
            sum += math.factorial(2*n) // (math.factorial(i) * math.factorial(j) * math.factorial(n-i) * math.factorial(n-j))
    return sum