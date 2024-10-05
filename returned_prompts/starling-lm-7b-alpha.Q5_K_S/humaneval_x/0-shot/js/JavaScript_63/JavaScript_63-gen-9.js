To solve this problem, you can use dynamic programming to store the intermediate results. Here's a step-by-step explanation:

1. Create an array called `fibfib` with a length of `n + 1` to store the Fibonacci numbers.
2. Set the first three elements of the `fibfib` array to 0, 0, and 1, respectively. This corresponds to `fibfib(0)`, `fibfib(1)`, and `fibfib(2)`.
3. Starting from the fourth element of the `fibfib` array, iterate through the array and calculate the Fibonacci number at each index by adding the previous three Fibonacci numbers: `fibfib[n] = fibfib[n-1] + fibfib[n-2] + fibfib[n-3]`.
4. After the iteration is complete, the Fibonacci number at index `n` is the result.

Here's the code that implements these steps:

```javascript
const fibfib = (n) => {
  const fibfib = Array(n + 1).fill(0);
  fibfib[0] = 0;
  fibfib[1] = 0;
  fibfib[2] = 1;

  for (let i = 3; i <= n; i++) {
    fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
  }

  return fibfib[n];
};
```

You can test the function with the provided examples:

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This approach has a time complexity of O(n) and a space complexity of O(n), which is efficient for most cases.

However, if you prefer a more concise solution that trades a small amount of efficiency for brevity, you can use the following code: