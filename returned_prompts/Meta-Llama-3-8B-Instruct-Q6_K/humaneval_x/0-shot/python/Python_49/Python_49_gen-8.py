```
def modp(n: int, p: int):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = modp(n // 2, p)
        return (half * half) % p
    else:
        return (n * modp(n - 1, p)) % p
```


The above function calculates 2^n modulo p using the exponentiation by squaring method, which is efficient for large values of n. If n is 0, the function returns 1, as any base raised to the power of 0 is 1. If n is even, the function calculates 2^(n/2) modulo p and squares the result. If n is odd, the function calculates 2^(n-1) modulo p and multiplies the result by n. This method avoids the need to compute 2^n directly, which can be computationally expensive for large values of n. The result is then returned modulo p to ensure that it is within the range [0, p).