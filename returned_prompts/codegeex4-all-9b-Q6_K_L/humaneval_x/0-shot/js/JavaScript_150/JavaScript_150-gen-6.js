You can use the built-in Math.sqrt function to determine if a number is prime. If a number is prime, it should only be divisible by 1 and itself. Here's how you can implement it in JavaScript:

```javascript
const xOrY = (n, x, y) => {
  if (n < 2) return y;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return y;
  }
  return x;
};
```

This function first checks if n is less than 2. If so, it immediately returns y because numbers less than 2 are not prime.

Next, it loops through numbers from 2 to the square root of n. If any of these numbers divide n evenly (i.e., the remainder is 0), then n is not a prime number and the function returns y.

If the function hasn't returned y yet, that means n is a prime number and the function returns x.