```java
const largestSmallestIntegers = (lst) => {
  let pos = lst.filter(e => e > 0).sort((a, b) => a - b)
  let neg = lst.filter(e => e < 0).sort((a, b) => b - a)
  return [neg.length ? neg[0] : null, pos.length ? pos[0] : null]
}
```
