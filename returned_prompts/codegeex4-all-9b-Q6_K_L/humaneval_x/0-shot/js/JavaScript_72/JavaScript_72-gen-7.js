```java
const willItFly = (q, w) => {
  if (q.reduce((a, b) => a + b, 0) > w) { return false }
  if (q.length == 1) { return true }
  if (q[0] == q[q.length - 1]) { return willItFly(q.slice(1, -1), w) }
  return false
}
```
