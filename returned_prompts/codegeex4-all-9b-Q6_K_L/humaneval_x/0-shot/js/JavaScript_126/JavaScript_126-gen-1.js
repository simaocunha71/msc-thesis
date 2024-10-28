```java
const isSorted = (lst) => {
  let p = lst[0]
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < p) return false
    p = lst[i]
  }
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] == lst[i + 1]) return false
  }
  return true
}
```
