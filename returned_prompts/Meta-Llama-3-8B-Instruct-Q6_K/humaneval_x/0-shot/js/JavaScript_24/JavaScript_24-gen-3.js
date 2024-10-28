Here is a simple JavaScript function that finds the largest number that divides `n` evenly, smaller than `n`:
```javascript
const largestDivisor = (n) => {
  for (let i = n - 1; i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
};
```
Here's an explanation of the code:

1. We start with `i` equal to `n - 1`, and decrement it until `i` is greater than 1.
2. We check if `n` is divisible by `i` using the modulo operator (`n % i === 0`). If it is, we've found the largest divisor smaller than `n`, so we return `i`.
3. If we reach the end of the loop without finding a divisor, we return 1, which is the trivial divisor of any number.

You can test the function with the example you provided:
```javascript
console.log(largestDivisor(15)); // Output: 5
```
This function has a time complexity of O(√n), since we're iterating from `n - 1` down to 1, and the number of iterations is bounded by the square root of `n`. For large values of `n`, this function may be slow. If you need a more efficient solution, you can use a more advanced algorithm, such as the Euclidean algorithm.