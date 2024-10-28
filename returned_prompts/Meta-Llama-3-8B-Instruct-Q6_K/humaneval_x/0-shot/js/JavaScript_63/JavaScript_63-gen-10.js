Here is the solution using memoization:
```
const fibfib = (n) => {
  const memo = { 0: 0, 1: 0, 2: 1 };
  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
  }
  return memo[n];
};
```
Explanation:

* We create a memoization object `memo` to store the previously computed values.
* We initialize the first three values of the sequence: `fibfib(0) == 0`, `fibfib(1) == 0`, and `fibfib(2) == 1`.
* We iterate from `i = 3` to `n` and compute the `i-th` element of the sequence using the recurrence relation: `fibfib(i) = fibfib(i-1) + fibfib(i-2) + fibfib(i-3)`.
* We store the computed value in the `memo` object.
* Finally, we return the `n-th` element of the sequence from the `memo` object.

This solution has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of `n`.

Note: You can also use dynamic programming to solve this problem, but memoization is a more efficient approach in this case.