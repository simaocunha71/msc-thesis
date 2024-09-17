
def newman_prime(n: int) -> int:
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        for i in range(1, n):
            j = newman_prime(i)
            k = newman_prime(n-i)
            if j * k >= 4 * 10**n:
                return j * k


