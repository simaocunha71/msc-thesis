You can solve this problem by using the concept of modular exponentiation. The idea is to compute (2^n) % p without directly computing 2^n, which could result in an integer overflow. 

Here is a Python solution for the problem:

```python
def modp(n, p):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modp(n // 2, p) ** 2 % p
    else:
        return (modp(n // 2, p) ** 2 * 2) % p

# Test the function
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

In this solution, if n is even, we compute (2^(n/2))^2 % p, and if n is odd, we compute ((2^(n/2))^2 * 2) % p. This is because (2^n) % p = ((2^(n/2))^2) % p if n is even, and (2^n) % p = ((2^(n/2))^2 * 2) % p if n is odd.

We use recursion to compute (2^n) % p for smaller values of n, and then use the results to compute (2^n) % p for larger values of n. This is an example of the divide-and-conquer algorithm.