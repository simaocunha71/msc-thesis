  if (n === 0 || n === 1) return 0;
  if (n === 2) return 1;

  let fibfib = [0, 0, 1];

  for (let i = 3; i <= n; i++) {
    fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3];
  }

  return fibfib[n];
};

console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24
```

This solution uses the iterative approach to calculate the nth FibFib number, storing the previous 3 numbers in an array. The time complexity of this solution is O(n), and the space complexity is also O(n).

If you need to find the FibFib numbers for large values of n, consider using an iterative approach with constant space complexity, since you only need to keep track of the last three numbers at any given time.

This problem is a variation of the Fibonacci sequence where each number is the sum of the previous three numbers. The sequence starts 0, 0, 1 and goes on as 0, 1, 1, 2, 4, 7, 13, 24, etc.

You can solve it using a dynamic programming approach where you store the previously computed values to avoid redundant calculations. The time complexity of this solution is O(n) and the space complexity is also O(n).

Here's the JavaScript code:

```javascript
const fibfib = (n) => {
  if (n === 0 || n === 1) return 0;
  if (n === 2) return 1;

  let fibfib = [0, 0, 1];

  for (let i = 3; i <= n; i++) {
    fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3];
  }

  return fibfib[n];
};
