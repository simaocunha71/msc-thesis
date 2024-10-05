```
const fib4 = (n) => {
  if (n <= 3) return [0, 0, 2, 0][n - 1];
  const fib4s = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fib4s[i - 1] = fib4s[i - 2] + fib4s[i - 3] + fib4s[i - 4];
  }
  return fib4s[n - 1];
};
```


Explanation:
The function fib4 takes an integer n as input and returns the nth element of the fib4 sequence. It uses a loop to calculate the sequence elements iteratively, starting from the base cases (n <= 3). For each iteration, it updates the current element as the sum of the previous three elements. The function returns the nth element as the result.

The base cases (n <= 3) are handled separately to avoid unnecessary calculations. The array fib4s is used to store the calculated sequence elements, and the loop iterates from i = 4 to n. The function returns the nth element as fib4s[n - 1]. This approach is more efficient than using recursion, as it avoids the overhead of function calls and returns.