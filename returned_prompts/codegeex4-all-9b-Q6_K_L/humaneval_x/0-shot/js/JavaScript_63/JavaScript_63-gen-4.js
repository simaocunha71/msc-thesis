```javascript
const fibfib = (n) => {
  let memo = [0, 0, 1];
  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
  }
  return memo[n];
};
```
