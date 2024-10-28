```js
const modp = (n, p) => {
  let r = 1;
  for (let i = 0; i < n; i++) {
    r = (2 * r) % p;
  }
  return r;
}
```
