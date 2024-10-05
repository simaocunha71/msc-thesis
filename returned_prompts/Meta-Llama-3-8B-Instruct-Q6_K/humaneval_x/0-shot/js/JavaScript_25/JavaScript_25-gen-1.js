```
const factorize = (n) => {
  const factors = [];
  let i = 2;
  while (i * i <= n) {
    while (n % i === 0) {
      factors.push(i);
      n = n / i;
    }
    i += 1;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
};
```


Explanation:
The given problem is to find all prime factors of a given integer `n` and return them as a list in the order from smallest to largest. Each factor should be listed the number of times it appears in the factorization.

The solution uses a simple algorithm to find the prime factors of the given number `n`. It starts by dividing `n` by the smallest prime number, which is 2, as long as `n` is divisible by 2. Then it increments the divisor by 1 and repeats the process until `n` is no longer divisible by the current divisor.

If `n` is still greater than 1 after the loop, it means that `n` is a prime number itself, so we add it to the list of factors.

The function returns the list of factors. For example, `factorize(8)` returns `[2, 2, 2]`, `factorize(25)` returns `[5, 5]`, and `factorize(70)` returns `[2, 5, 7]`.

Time complexity: O(sqrt(n))
Space complexity: O(1) (assuming the size of the output list is not considered)