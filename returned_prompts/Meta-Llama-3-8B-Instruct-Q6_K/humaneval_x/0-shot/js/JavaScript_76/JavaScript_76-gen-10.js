Here is the solution for the problem:
```javascript
const isSimplePower = (x, n) => {
  if (n <= 0) {
    return false;
  }
  let base = 1;
  while (base * base <= x) {
    if (base * base === x) {
      return true;
    }
    base++;
  }
  return false;
};
```
Here is an explanation of the solution:

1. First, we check if `n` is less than or equal to 0. If it is, we immediately return `false`, because `n` must be a positive integer.
2. We initialize a variable `base` to 1, which will be used to calculate the powers of `n`.
3. We loop until `base * base` is greater than `x`. In each iteration, we check if `base * base` is equal to `x`. If it is, we return `true`, because `x` is a simple power of `n`.
4. If the loop completes without finding a match, we return `false`, because `x` is not a simple power of `n`.

This solution works because it checks all possible powers of `n` up to `x`, and returns `true` as soon as it finds a match. If no match is found, it returns `false`. The time complexity of this solution is O(sqrt(x)), because we only need to check up to the square root of `x` to find a match. The space complexity is O(1), because we only use a constant amount of space to store the variables.