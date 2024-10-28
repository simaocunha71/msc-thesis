```java
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) return -1
  return ((a + b + c) / 2) * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c) / 4
}
```
