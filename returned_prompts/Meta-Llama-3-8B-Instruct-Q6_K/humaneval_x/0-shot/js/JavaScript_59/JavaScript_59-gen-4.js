Here is a solution for the problem:
```
const largestPrimeFactor = (n) => {
  let maxPrimeFactor = 1;
  for (let i = 2; i * i <= n; i++) {
    while (n % i === 0) {
      maxPrimeFactor = i;
      n = n / i;
    }
  }
  if (n > 1) {
    maxPrimeFactor = n;
  }
  return maxPrimeFactor;
};
```


Explanation:
The solution iterates through all numbers from 2 to the square root of `n`, and for each number `i`, it checks if `n` is divisible by `i`. If it is, it divides `n` by `i` and updates `maxPrimeFactor` to be the current value of `i`. This process continues until `n` is no longer divisible by `i`. If `n` is still greater than 1 at this point, it means that `n` itself is a prime number, and `maxPrimeFactor` is updated to be `n`. Finally, the function returns `maxPrimeFactor`.

The reason for stopping at `i * i <= n` is that if `i` is a prime factor of `n`, then `i` must be less than or equal to the square root of `n`, because if `i` were greater than the square root of `n`, then `n / i` would be less than `i`, and therefore not a prime factor of `n`. This optimization reduces the number of iterations and makes the function more efficient.