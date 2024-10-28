Here is a simple function that finds the largest divisor of a given number `n`:
```
const largestDivisor = (n) => {
  for (let i = n - 1; i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
};
```
Here's an explanation of how the function works:

1. We start by iterating from `n - 1` down to `1` using a `for` loop.
2. For each iteration, we check if `n` is divisible by the current number `i` using the modulo operator (`%`). If the remainder is `0`, it means that `i` is a divisor of `n`.
3. If we find a divisor, we immediately return it. If we reach the end of the loop without finding a divisor, it means that `1` is the largest divisor (since `n` is always divisible by `1`).
4. The function returns the largest divisor found, or `1` if no divisors were found.

You can test the function with the example you provided:
```
console.log(largestDivisor(15)); // Output: 5
```
This function has a time complexity of O(n), where `n` is the input number. This is because we iterate up to `n` times in the worst case. However, in practice, the function is usually much faster because it terminates as soon as it finds a divisor.