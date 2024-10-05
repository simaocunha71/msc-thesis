```java
const triangleArea = (a, b, c) => {
  let s = (a + b + c) / 2.0
  let area = Math.sqrt(s * (s - a) * (s - b) * (s - c))
  if (area != area) {
    return -1
  }
  return Number(area.toFixed(2))
}
```
