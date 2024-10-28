```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```


The code defines a function `isPrime` that takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

Here's a breakdown of the code:

1. `if (n <= 1) return false;`: This line checks if `n` is less than or equal to 1. If it is, the function immediately returns `false`, because numbers less than or equal to 1 are not prime.
2. `for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)`: This loop iterates from 2 to the square root of `n` (inclusive). The `sqrt` variable is used to optimize the loop by reducing the number of iterations.
3. `if (n % i === 0) return false;`: Inside the loop, this line checks if `n` is divisible by `i`. If it is, the function returns `false`, because `n` is not prime.
4. `return true;`: If the loop completes without finding a divisor, the function returns `true`, indicating that `n` is prime.

The function uses the property that a composite number must have a factor less than or equal to its square root. This allows us to efficiently check for primality by only considering divisors up to the square root of `n`.