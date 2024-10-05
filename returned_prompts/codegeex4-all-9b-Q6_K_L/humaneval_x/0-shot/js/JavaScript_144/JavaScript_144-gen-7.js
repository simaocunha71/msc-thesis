```java
const simplify = (x, n) => {
  let numerator = parseInt(x.split('/')[0]) * parseInt(n.split('/')[0]);
  let denominator = parseInt(x.split('/')[1]) * parseInt(n.split('/')[1]);
  return numerator % denominator == 0;
}
```