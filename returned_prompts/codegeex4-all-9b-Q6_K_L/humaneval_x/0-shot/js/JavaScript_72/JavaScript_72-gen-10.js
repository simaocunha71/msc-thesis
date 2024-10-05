```java
const willItFly = (q, w) => {
  let left = 0
  let right = q.length - 1
  let sum = 0
  while (left <= right) {
    sum += q[left] + q[right]
    left++
    right--
  }
  return sum <= w && q.length % 2 == 0
}
```
