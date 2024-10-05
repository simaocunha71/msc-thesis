```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```


Explanation:
The function `isPrime` takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

1. If `n` is less than or equal to 1, it is not prime, so the function returns `false`.
2. The function then iterates from 2 to the square root of `n` (inclusive) using a `for` loop. This is because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.
3. Inside the loop, the function checks if `n` is divisible by the current number `i` using the modulo operator (`%`). If `n` is divisible by `i`, it means that `n` has a factor other than 1 and itself, so the function returns `false`.
4. If the loop completes without finding a divisor, the function returns `true`, indicating that `n` is prime.

The time complexity of this function is O(√n), which is efficient for large values of `n`. The space complexity is O(1), as it only uses a constant amount of space to store the loop variable and the result.