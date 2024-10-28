```java
const willItFly = (q, w) => {
  if (q.reduce((prev, item) => prev + item, 0) > w) { return false; }
  for (let i = 0; i < q.length / 2; i++) {
    if (q[i] !== q[q.length - 1 - i]) { return false; }
  }
  return true;
}
```
