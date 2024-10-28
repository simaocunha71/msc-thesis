You can solve this problem using the method of exponentiation by squaring. This method reduces the number of operations required to calculate the power of a number. Here's how you can implement this in JavaScript:

```javascript
const modp = (n, p) => {
  if (n === 0) return 1;
  let result = 1;
  let x = n;
  while (p > 0) {
    if (p % 2 === 1) {
      result = (result * x) % p;
    }
    x = (x * x) % p;
    p = Math.floor(p / 2);
  }
  return result;
};
```

In this function, `n` is the base and `p` is the exponent. The function first checks if `n` is 0, in which case it returns 1. Then it initializes `result` and `x` to 1 and `n`, respectively, and starts a loop that continues until `p` is 0. In each iteration of the loop, the function checks if `p` is odd. If it is, it multiplies `result` by `x` and takes the result modulo `p`. Then it squares `x` and takes the result modulo `p`, and divides `p` by 2 using `Math.floor`. Finally, the function returns `result`.