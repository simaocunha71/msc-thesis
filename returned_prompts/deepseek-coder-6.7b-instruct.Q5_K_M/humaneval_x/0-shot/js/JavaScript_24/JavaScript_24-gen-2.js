  for(let i = n - 1; i > 0; i--) {
    if(n % i === 0) {
      return i;
    }
  }
}

console.log(largestDivisor(15)); // 5
```

This solution works by iterating from `n-1` down to `1`. For each number `i`, it checks whether `n` is divisible by `i` with no remainder (`n % i === 0`). If `n` is divisible by `i`, it immediately returns `i`. If no such number `i` is found, the function returns `undefined`.

However, there is a more efficient solution:

```javascript
const largestDivisor = (n) => {
  for(let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
    if(n % i === 0) {
      return n / i;
    }
  }
  return 1;
}

console.log(largestDivisor(15)); // 5
```

In this solution, we loop from `2` up to the square root of `n`. If `n` is divisible by `i`, then `n / i` is the largest divisor. If `n` is not divisible by any `i`, then `1` is the largest divisor.

This solution is more efficient because it only needs to check divisors up to the square root of `n`, and it avoids unnecessary checks by only considering pairs of factors.

**Note:** The function `Math.floor(Math.sqrt(n))` returns the largest integer less than or equal to the square root of `n`. This is because for a number `n`, its largest divisor can't be larger than the square root of `n`.

**Note:** This function will return `1` if `n` is a prime number, because a prime number has no divisors other than `1` and itself.

**Note:** In JavaScript, the `%` operator returns the remainder of the division. If `n % i === 0`, then `n` is divisible by `i`.

**Note: