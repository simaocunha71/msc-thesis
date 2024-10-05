```java
const modp = (n, p) => {
  let result = 1;
  while (n > 0) {
    if (n % 2 === 1) {
      result = (result * 2) % p;
    }
    n = Math.floor(n / 2);
    p = (p * p) % 1024;
  }
  return result;
}
```