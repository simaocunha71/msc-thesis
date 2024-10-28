```java
const isSorted = (lst) => {
  let prev = lst[0]
  let duplicates = {}
  for (let i = 1; i < lst.length; i++) {
    if (duplicates[lst[i]]) {
      return false
    }
    if (lst[i] <= prev) {
      return false
    }
    duplicates[prev] = true
    prev = lst[i]
  }
  return true
}
```
