To solve this problem, we can use a dynamic programming approach to build up the fibfib number sequence until we reach the n-th element. We'll store the fibfib numbers in an array and use memoization to avoid redundant calculations.

Here's the solution:

```javascript
const fibfib = (n) => {
  // Initialize an array to store the fibfib numbers
  const fibfibNumbers = [0, 0, 1];

  // Build up the fibfib number sequence until we reach the n-th element
  for (let i = 3; i <= n; i++) {
    fibfibNumbers[i] = fibfibNumbers[i - 1] + fibfibNumbers[i - 2] + fibfibNumbers[i - 3];
  }

  // Return the n-th element of the fibfib number sequence
  return fibfibNumbers[n];
};
```

Let's test the solution with the provided test cases:

```javascript
console.log(fibfib(1)); // Output: 0
console.log(fibfib(5)); // Output: 4
console.log(fibfib(8)); // Output: 24
```

The output is as expected.