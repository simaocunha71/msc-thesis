```
const modp = (n, p) => {
  if (n === 0) return 1;
  if (n % 2 === 0) {
    const half = modp(n / 2, p);
    return (half * half) % p;
  }
  return (n * modp(n - 1, p)) % p;
};
```


The function `modp` calculates `2^n modulo p` using the property of modular arithmetic that `(a * b) % p = ((a % p) * (b % p)) % p`. It does this by recursively dividing `n` by 2 until `n` is 0, and then using the result to calculate the final answer. This approach is known as exponentiation by squaring, and it is more efficient than repeatedly multiplying `2` by itself `n` times. The base case for the recursion is when `n` is 0, in which case the function returns 1. If `n` is even, the function calls itself with `n` divided by 2, and then squares the result. If `n` is odd, the function calls itself with `n - 1`, and then multiplies the result by `n`. The final result is then taken modulo `p`. This approach avoids the need to calculate large intermediate results, which can help to avoid overflows.