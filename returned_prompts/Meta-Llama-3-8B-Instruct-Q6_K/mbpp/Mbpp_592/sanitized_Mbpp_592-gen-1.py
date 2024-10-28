def sum_Of_product(n):
    sum = 0
    for i in range(1, n+1):
        sum += binom(i,1)*binom(i,2)
    return sum
def binom(n, k):
    if k > n:
        return 0
    if k > n//2:
        k = n-k
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) // i
    return result