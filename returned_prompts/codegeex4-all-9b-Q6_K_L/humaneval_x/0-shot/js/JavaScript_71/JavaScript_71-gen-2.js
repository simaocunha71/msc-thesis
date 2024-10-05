```java
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) return -1;
  let p = (a + b + c) / 2;
  let area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
  return Math.round(area * 100) / 100;
}
```
