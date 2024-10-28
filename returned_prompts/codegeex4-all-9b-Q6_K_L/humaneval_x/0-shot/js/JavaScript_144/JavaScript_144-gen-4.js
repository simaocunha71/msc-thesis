```java
const simplify = (x, n) => {
  const a = x.split(/\//);
  const b = n.split(/\//);
  const numerator = Number(a[0]) * Number(b[0]);
  const denominator = Number(a[1]) * Number(b[1]);
  return numerator % denominator === 0;
}
```
