To efficiently compute the n-th element of the fibfib number sequence, you can use dynamic programming to store the previously computed values and avoid redundant calculations. Here's an implementation of the fibfib function:

```javascript
const fibfib = (n) => {
  // Create an array to store the previously computed values
  const fibfibValues = [0, 0, 1];

  // Compute the fibfib values from 3 to n
  for (let i = 3; i <= n; i++) {
    fibfibValues[i] = fibfibValues[i - 1] + fibfibValues[i - 2] + fibfibValues[i - 3];
  }

  // Return the n-th fibfib value
  return fibfibValues[n];
};
```

This implementation has a time complexity of O(n) and a space complexity of O(n).