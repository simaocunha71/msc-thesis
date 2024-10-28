```
  if (n <= 1) return false;
  if (n === 2) return true;
  if (n % 2 === 0) return false;

  const max = Math.sqrt(n);

  for (let i = 3; i <= max; i += 2) {
    if (n % i === 0) return false;
  }

  return true;
};
```


Explanation:
The function takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

1. First, we handle the edge cases: if `n` is less than or equal to 1, it's not prime, so we return `false`. If `n` is 2, it's prime, so we return `true`.
2. If `n` is even, it's not prime, so we return `false`.
3. We then calculate the maximum possible divisor `max` by taking the square root of `n`. This is because any factor larger than the square root would have a corresponding factor smaller than the square root.
4. We then iterate from 3 to `max` in increments of 2 (since we've already handled even numbers). For each potential divisor `i`, we check if `n` is divisible by `i` by using the modulo operator (`n % i === 0`). If it is, `n` is not prime, so we return `false`.
5. If we reach the end of the loop without finding a divisor, `n` is prime, so we return `true`.

This function uses a combination of early returns and a loop to efficiently determine whether a given number is prime or not. It has a time complexity of O(√n), which is relatively fast for large inputs.