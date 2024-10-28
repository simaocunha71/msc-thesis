```
const modp = (n, p) => {
  if (n === 0) return 1;
  if (n % 2 === 0) {
    const halfMod = modp(n / 2, p);
    return (halfMod * halfMod) % p;
  } else {
    return (n * modp(n - 1, p)) % p;
  }
};
```


Explanation:
This function uses the property of modular arithmetic that `a * b mod p = (a mod p) * (b mod p) mod p`. It also uses the fact that `2^(n/2) mod p = (2^(n/2) mod p) * (2^(n/2) mod p) mod p` if `n` is even.

The function first checks if `n` is 0, in which case it returns 1 since `2^0 mod p = 1`.

If `n` is even, the function recursively calls itself with `n` divided by 2 and multiplies the results together.

If `n` is odd, the function recursively calls itself with `n-1` and multiplies the result by `n`.

Finally, the function returns the result of the multiplication modulo `p`. This ensures that the result is always between 0 and `p-1`.