```
def modp(n: int, p: int):
    return pow(n, p-2, p)
```

Explanation:
The function `modp(n, p)` calculates 2^n modulo p. The `pow()` function in Python can be used to calculate this efficiently, especially for large values of n.

The `pow()` function takes three arguments: the base `n`, the exponent `p-2`, and the modulus `p`. The result is the value of `n` raised to the power `p-2` modulo `p`.

This function works well for large values of `n` because it uses the property of modular arithmetic that `a^(p-1) ≡ 1 (mod p)` for any integer `a` not divisible by `p`. This property allows us to calculate `a^(p-2)` modulo `p` efficiently, without having to calculate the full power.

For example, if `p` is 101, then `pow(2, 99, 101)` is equivalent to `2^99` modulo 101. This is much faster and more efficient than calculating `2^99` directly and then taking the modulus.