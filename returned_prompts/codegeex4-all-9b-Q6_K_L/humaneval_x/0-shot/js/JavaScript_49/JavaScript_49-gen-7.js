```java
const modp = (n, p) => {
  if (n === 0) return 1;
  let half = modp(n >> 1, p);
  half = (half * half) % p;
  if (n & 1) half = (half * 3) % p;
  return half;
}
```
