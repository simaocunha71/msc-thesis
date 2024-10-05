```javascript
const modp = (n, p) => {
  let result = 1;
  n = n % p;
  while (n > 0) {
    if (n % 2 !== 0) {
      result = (result * n) % p;
    }
    n = Math.floor(n / 2);
  }
  return result;
};
```


This code calculates 2^n modulo p using the property of modular exponentiation. It iterates through the binary representation of n, and for each '1' in the binary representation, it multiplies the current result by n modulo p. The result is the value of 2^n modulo p.

The key insight is that we can calculate 2^(2n) modulo p by squaring 2^n modulo p, and then reducing the result modulo p. This allows us to reduce the number of multiplications needed, making the algorithm more efficient.

In the code above, we initialize the result to 1, and then iterate through the binary representation of n. For each '1' in the binary representation, we multiply the result by n modulo p. We then reduce the result modulo p to ensure that it remains within the range [0, p-1].

Finally, we return the result, which is the value of 2^n modulo p. This algorithm has a time complexity of O(log n), making it efficient for large values of n.

Note that we use the modulo operation (%) to ensure that the result remains within the range [0, p-1]. This is important to avoid overflow and ensure that the result is accurate.