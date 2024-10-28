```java
const willItFly = (q, w) => {
  let sum = 0
  for (let i = 0; i < q.length; i++) {
    if (q[i] != q[q.length - i - 1]) {
      return false
    }
    sum += q[i]
  }
  return sum <= w
}
```
