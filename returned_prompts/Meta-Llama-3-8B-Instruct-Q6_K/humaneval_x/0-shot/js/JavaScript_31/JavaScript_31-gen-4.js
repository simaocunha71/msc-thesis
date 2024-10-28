```javascript
const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};
```
The function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the values. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of the values, the function returns `true`, indicating that the number is prime.

Note: The condition `i * i <= n` is used to optimize the loop, as any factor greater than the square root of the number would have a corresponding factor less than the square root, which would have been checked already. This reduces the number of iterations and improves the efficiency of the function.