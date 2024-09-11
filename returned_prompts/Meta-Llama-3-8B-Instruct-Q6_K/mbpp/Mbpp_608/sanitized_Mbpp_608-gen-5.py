def bell_Number(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return sum(binomial(n, k) for k in range(n))
def binomial(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result