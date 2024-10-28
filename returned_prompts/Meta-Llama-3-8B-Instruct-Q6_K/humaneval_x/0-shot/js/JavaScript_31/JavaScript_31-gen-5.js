```javascript
const isPrime = (n) => {
  if (n <= 1) return false; // 0 and 1 are not prime
  if (n === 2) return true; // 2 is prime
  if (n % 2 === 0) return false; // all other even numbers are not prime

  for (let i = 3; i * i <= n; i += 2) {
    if (n % i === 0) return false; // if n is divisible by any number between 2 and sqrt(n), it's not prime
  }
  return true; // if n is not divisible by any number between 2 and sqrt(n), it's prime
};
```


Explanation:
The function `isPrime` takes an integer `n` as input and returns `true` if it's prime, and `false` otherwise.

1. If `n` is less than or equal to 1, it's not prime, so we return `false`.
2. If `n` is 2, it's prime, so we return `true`.
3. If `n` is an even number greater than 2, it's not prime, so we return `false`.
4. We then iterate from 3 to the square root of `n` (inclusive) with a step size of 2. For each number `i` in this range, we check if `n` is divisible by `i` using the modulo operator (`n % i === 0`). If it is, `n` is not prime, so we return `false`.
5. If `n` is not divisible by any number in this range, it's prime, so we return `true`.