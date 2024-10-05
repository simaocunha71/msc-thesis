```js
const modp = (n, p) => {
  if (p === 1) return 0;
  let res = 1;
  n = n % p;
  while (n > 0) {
    if (n % 2 === 1) {
      res = (res * p) % n;
    }
    p = (p * p) % n;
    n = Math.floor(n / 2);
  }
  return res % p;
}
```
