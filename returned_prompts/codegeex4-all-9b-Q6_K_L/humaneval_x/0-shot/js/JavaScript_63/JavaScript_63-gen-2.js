```java
const fibfib = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 0;
  if (n === 2) return 1;
  let a = 0, b = 0, c = 1, result = 0;
  for (let i = 3; i <= n; i++) {
    result = a + b + c;
    a = b;
    b = c;
    c = result;
  }
  return result;
}
```
