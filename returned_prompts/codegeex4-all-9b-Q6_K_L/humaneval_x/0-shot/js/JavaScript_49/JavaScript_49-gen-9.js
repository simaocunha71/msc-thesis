```java
const modp = (n, p) => {
  if (n == 0)
    return 1;
  let res = modp(n / 2, p);
  res = (res * res) % p;
  if (n % 2 != 0)
    res = (res * 2) % p;
  return res;
}
```