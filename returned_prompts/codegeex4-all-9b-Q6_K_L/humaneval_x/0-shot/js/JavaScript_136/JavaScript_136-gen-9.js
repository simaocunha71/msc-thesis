```java
const largestSmallestIntegers = (lst) => {
  let pos = lst.filter(x => x > 0)
  let neg = lst.filter(x => x < 0)
  return [neg.length ? Math.max(...neg) : null, pos.length ? Math.min(...pos) : null]
}
```
