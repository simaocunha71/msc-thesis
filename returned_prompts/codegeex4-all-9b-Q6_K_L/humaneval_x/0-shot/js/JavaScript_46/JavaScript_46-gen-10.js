```javascript
  let memo = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3] + memo[i - 4];
  }
  return memo[n];
};
```