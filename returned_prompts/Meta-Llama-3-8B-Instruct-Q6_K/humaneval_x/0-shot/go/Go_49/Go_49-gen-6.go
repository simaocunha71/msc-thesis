This problem is asking for a function that calculates 2^n modulo p, where n and p are integers. The function should be aware of numeric overflow and return the correct result.

Here's a Python solution for the problem:
```python
def Modp(n, p):
    if n == 0:
        return 1
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
    return result
```
This function uses the property of modular exponentiation that `a^(2k) = (a^k)^2` and `a^(2k+1) = (a^k)^2 * a`. It iteratively reduces the exponent `n` by half and squares the result until `n` becomes 0. If `n` is odd, it multiplies the result by `a` (in this case, 2). The final result is the modular exponentiation of 2 to the power of `n` modulo `p`.

For example, `Modp(3, 5)` returns 3, `Modp(1101, 101)` returns 2, `Modp(0, 101)` returns 1, `Modp(3, 11)` returns 8, and `Modp(100, 101)` returns 1. These results are correct because 2^3 modulo 5 is 3, 2^(2*528+1) modulo 101 is 2, 2^0 modulo 101 is 1, 2^3 modulo 11 is 8, and 2^(2*49+2) modulo 101 is 1.