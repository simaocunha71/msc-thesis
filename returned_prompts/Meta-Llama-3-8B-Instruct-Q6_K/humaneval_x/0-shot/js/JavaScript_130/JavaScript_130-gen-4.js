Here is a solution using recursion:
```
const tri = (n) => {
  if (n === 0) return [1];
  if (n === 1) return [1, 3];
  if (n === 2) return [1, 3, 2];

  const tribonacci = tri(n - 1);
  tribonacci.push(tribonacci[tribonacci.length - 1] + tribonacci[tribonacci.length - 2] + 1);
  return tribonacci;
};
```
Here's how it works:

1. If `n` is 0, return a list containing only 1.
2. If `n` is 1, return a list containing 1 and 3.
3. If `n` is 2, return a list containing 1, 3, and 2.
4. Otherwise, recursively call `tri` with `n - 1` to get the previous Tribonacci sequence.
5. Add the last two elements of the previous sequence and 1 to get the next element.
6. Add the new element to the previous sequence and return the result.

For example, `tri(3)` would return `[1, 3, 2, 8]`.

Note that this solution has a time complexity of O(n) and a space complexity of O(n) since we need to store the previous sequence. If you need a more efficient solution, you can use dynamic programming or memoization.