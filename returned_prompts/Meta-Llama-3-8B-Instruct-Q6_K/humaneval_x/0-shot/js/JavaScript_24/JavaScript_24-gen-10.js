```javascript
const largestDivisor = (n) => {
  for (let i = n - 1; i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
};

console.log(largestDivisor(15)); // Output: 5
```
The function `largestDivisor` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`.

The function uses a for loop to iterate from `n - 1` down to `2`. For each number `i` in this range, it checks if `n` is divisible by `i` by using the modulo operator (`n % i === 0`). If `n` is divisible by `i`, then `i` is the largest divisor of `n` smaller than `n`, and the function returns `i`.

If the loop completes without finding a divisor, then the function returns `1`, which is the smallest positive integer and the only number that divides `1` evenly.

In the example, `largestDivisor(15)` returns `5`, which is the largest number that divides `15` evenly, smaller than `15`.