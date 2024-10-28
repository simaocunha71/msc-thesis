```js
const fib4 = (n) => {
  const fib = [0, 0, 2, 0];
  if (n < 4) {
    return fib[n];
  }
  for (let i = 4; i <= n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4];
  }
  return fib[n];
};
```