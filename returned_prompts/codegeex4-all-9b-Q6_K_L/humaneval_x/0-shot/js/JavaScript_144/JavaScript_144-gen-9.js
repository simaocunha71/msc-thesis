```java
const simplify = (x, n) => {
  let a = x.split('/').map(Number);
  let b = n.split('/').map(Number);
  return (a[0] * b[1]) % (a[1] * b[0]) === 0;
}
```
