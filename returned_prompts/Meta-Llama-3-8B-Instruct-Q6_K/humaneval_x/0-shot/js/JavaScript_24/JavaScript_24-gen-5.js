```javascript
const largestDivisor = (n) => {
  for(let i = n - 1; i > 1; i--) {
    if(n % i === 0) {
      return i;
    }
  }
  return 1;
};
```


Explanation:

1. The function `largestDivisor` takes an integer `n` as input.
2. It iterates from `n - 1` down to `2` (inclusive) using a `for` loop.
3. For each iteration, it checks if `n` is divisible by the current number `i` using the modulo operator (`%`). If the remainder is `0`, it means `i` is a divisor of `n`.
4. If a divisor is found, the function returns that divisor.
5. If no divisor is found, the function returns `1`, which is the trivial divisor of every number.

Note: This function has a time complexity of O(n), which may not be efficient for large values of `n`. A more efficient solution would be to use a prime factorization algorithm, which would have a time complexity of O(sqrt(n)). However, the above implementation is simple and works well for smaller values of `n`.