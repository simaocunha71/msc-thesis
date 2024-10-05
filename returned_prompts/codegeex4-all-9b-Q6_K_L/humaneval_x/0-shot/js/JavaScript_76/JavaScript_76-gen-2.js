```java
const isSimplePower = (x, n) => {
  if (x === 1) return true;
  if (x % n !== 0) return false;
  while (x % n === 0) {
    x /= n;
  }
  return x === 1;
}
```
