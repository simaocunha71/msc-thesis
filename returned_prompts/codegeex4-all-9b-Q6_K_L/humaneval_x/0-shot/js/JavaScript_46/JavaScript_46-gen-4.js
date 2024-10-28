```javascript
const fib4 = (n) => {
  const fib4Arr = [0, 0, 2, 0];
  if (n < 4) {
    return fib4Arr[n];
  }
  for (let i = 4; i <= n; i++) {
    fib4Arr[i] = fib4Arr[i - 1] + fib4Arr[i - 2] + fib4Arr[i - 3] + fib4Arr[i - 4];
  }
  return fib4Arr[n];
};
```