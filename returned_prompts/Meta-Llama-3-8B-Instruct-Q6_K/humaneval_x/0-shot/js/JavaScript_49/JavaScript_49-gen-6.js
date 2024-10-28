You can solve this problem using the properties of modular arithmetic. Specifically, you can use the fact that `a^(p-1) ≡ 1 (mod p)` for any integer `a` not divisible by `p`. This is known as Fermat's Little Theorem.

Here's the implementation:
```python
const modp = (n, p) => {
  if (n === 0) return 1;
  if (n % p === 0) return 0;
  return Math.pow(n, p-1) % p;
}
```
Here's an explanation of the code:

* If `n` is 0, the result is always 1, since `0^(p-1) = 1 (mod p)`.
* If `n` is a multiple of `p`, the result is 0, since `a^(p-1) = 0 (mod p)` for any `a` that is a multiple of `p`.
* Otherwise, we use the fact that `a^(p-1) ≡ 1 (mod p)` to compute the result. We use the `Math.pow` function to raise `n` to the power of `p-1`, and then take the remainder modulo `p` using the `%` operator.

This implementation should work for all positive integers `n` and `p`. Note that it's not necessary to handle the case where `n` is negative, since the properties of modular arithmetic still hold for negative integers. However, if you want to handle negative integers, you can simply add an additional check to handle the case where `n < 0`. For example:
```python
const modp = (n, p) => {
  if (n < 0) n = -n;
  if (n === 0) return 1;
  if (n % p === 0) return 0;
  return Math.pow(n, p-1) % p;
}
```
This implementation will work for all integers `n` and `p`.