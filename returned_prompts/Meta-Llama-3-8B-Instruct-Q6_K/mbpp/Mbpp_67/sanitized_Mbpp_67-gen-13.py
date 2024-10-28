def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum([(-1)**i * binomial(n, i) * bell_number(n-1) for i in range(n+1)])
def binomial(n, k):
    if k > n//2:
        k = n-k
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) // i
    return result