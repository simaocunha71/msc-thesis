```java
const triangleArea = (a, b, c) => {
  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    return ((s * (s - a) * (s - b) * (s - c)) ** 0.5).toFixed(2);
  }
  return -1;
}
```
