```js
const largestPrimeFactor = (n) => {
  let i = 2;
  while (i * i <= n) {
    if (n % i === 0) {
      n = n / i;
    } else {
      i += 1;
    }
  }
  return n;
}
```