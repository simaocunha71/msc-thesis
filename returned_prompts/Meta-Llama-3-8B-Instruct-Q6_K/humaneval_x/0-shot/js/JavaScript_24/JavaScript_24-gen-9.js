```javascript
function largestDivisor(n) {
  for (let i = n - 1; i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
}

console.log(largestDivisor(15)); // outputs 5
```
Explanation:
The function `largestDivisor` takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than `n`.

The function uses a for loop to iterate from `n-1` down to `2` (since 1 is not a proper divisor). For each iteration, it checks if `n` is divisible by the current number `i` using the modulo operator `%`. If it is divisible, it returns `i` as the largest divisor.

If no divisor is found, the function returns `1`, which is the trivial case where `n` is a prime number.

In the example, `largestDivisor(15)` returns `5` because 5 is the largest integer that divides 15 evenly, smaller than 15.