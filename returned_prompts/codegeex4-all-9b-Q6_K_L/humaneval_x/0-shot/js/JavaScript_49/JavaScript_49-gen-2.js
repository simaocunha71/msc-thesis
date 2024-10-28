```java
const modp = (n, p) => {
  if (n === 0) return 1;
  let res = 1;
  let base = n;
  while (base > 0) {
    if (base % 2 === 1) {
      res = (res * n) % p;
    }
    n = (n * n) % p;
    base = Math.floor(base / 2);
  }
  return res;
}
```
