```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  if (n === 2) return true;
  if (n % 2 === 0) return false;

  const maxDivisor = Math.floor(Math.sqrt(n));

  for (let i = 3; i <= maxDivisor; i += 2) {
    if (n % i === 0) return false;
  }

  return true;
};
```


Explanation:
The function checks if a given number `n` is prime or not. 

1. If `n` is less than or equal to 1, it's not prime, so return `false`.
2. If `n` is 2, it's prime, so return `true`.
3. If `n` is even (i.e., `n % 2 === 0`), it's not prime, so return `false`.
4. Calculate the maximum possible divisor by taking the square root of `n` and flooring it.
5. Iterate from 3 to the maximum possible divisor, incrementing by 2 (to check for odd numbers only).
6. For each number `i` in the iteration, check if `n` is divisible by `i` (i.e., `n % i === 0`). If it is, `n` is not prime, so return `false`.
7. If the loop completes without finding a divisor, `n` is prime, so return `true`.