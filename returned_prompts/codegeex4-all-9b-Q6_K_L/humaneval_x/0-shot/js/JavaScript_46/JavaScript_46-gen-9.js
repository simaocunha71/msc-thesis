```js
const fib4 = (n) => {
  if (n < 2) return 0;
  if (n === 2) return 2;
  if (n === 3) return 0;
  let a = 0, b = 0, c = 2, d = 0, result = 0;
  for (let i = 4; i <= n; i++) {
    result = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = result;
  }
  return result;
};
```
