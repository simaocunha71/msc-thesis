```java
const willItFly = (q, w) => {
  if (q.length == 1) {
    return q[0] <= w
  }
  if (q[0] != q[q.length - 1]) {
    return false
  }
  return willItFly(q.slice(1, q.length - 1), w - q[0] - q[q.length - 1])
}
```
