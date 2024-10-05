Here is the JavaScript code to solve the problem:

```javascript
const roundedAvg = (n, m) => {
  if (n > m) return -1;
  const sum = Array.from({ length: m - n + 1 }, (_, i) => n + i).reduce((acc, curr) => acc + curr, 0);
  const avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
};
```

Explanation:
1. The function takes two arguments `n` and `m` and checks if `n` is greater than `m`. If it is, the function returns `-1`.
2. It calculates the sum of the integers from `n` to `m` using the `Array.from` method to create an array of integers and the `reduce` method to sum them up.
3.