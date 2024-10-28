```java
const simplify = (x, n) => {
  let numerator = x.split('/')[0] * n.split('/')[0]
  let denominator = x.split('/')[1] * n.split('/')[1]
  return numerator % denominator == 0
}
```
