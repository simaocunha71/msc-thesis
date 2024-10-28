Here is the solution using a loop to iterate through all the numbers from 2 to n and check if they are prime factors of n. If a prime factor is found, it is compared with the current largest prime factor and updated if necessary.
```javascript
const largestPrimeFactor = (n) => {
  let largestPF = 1;
  for (let i = 2; i <= n; i++) {
    if (n % i === 0) {
      let isPF = true;
      for (let j = 2; j * j <= i; j++) {
        if (i % j === 0) {
          isPF = false;
          break;
        }
      }
      if (isPF) {
        largestPF = i;
      }
    }
  }
  return largestPF;
};
```
This function has a time complexity of O(n^2) due to the inner loop that checks if a number is prime. This can be optimized by using a more efficient primality test, such as the Miller-Rabin primality test, which has a time complexity of O(k \* log^3 n), where k is a small constant. However, for small values of n, the simple loop-based approach is sufficient.

For example, the output of the function for `largestPrimeFactor(13195)` is `29`, and for `largestPrimeFactor(2048)` is `2`. The function correctly returns the largest prime factor of the input number.