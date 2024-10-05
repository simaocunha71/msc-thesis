```java
const willItFly = (q, w) => {
  var l = 0, r = q.length - 1, sum = 0
  while (l <= r) {
    if (q[l] != q[r]) return false
    sum += q[l]
    l++
    r--
  }
  if (sum <= w) return true
  return false
}
```
