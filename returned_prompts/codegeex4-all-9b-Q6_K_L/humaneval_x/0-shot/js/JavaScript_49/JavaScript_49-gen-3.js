```java
const modp = (n, p) => {
  if (n == 0) return 1;
  var t = modp(n / 2, p);
  if (n % 2 == 0) return (t * t) % p;
  return ((t * t) % p) * 3 % p;
}
```
