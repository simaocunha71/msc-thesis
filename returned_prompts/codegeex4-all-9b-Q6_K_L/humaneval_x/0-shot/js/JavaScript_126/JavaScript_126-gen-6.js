```java
const isSorted = (lst) => {
  if (lst.length < 2) {
    return true
  }
  let prev = lst[0]
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < prev) {
      return false
    }
    if (lst[i] === prev) {
      for (let j = i + 1; j < lst.length; j++) {
        if (lst[j] === prev) {
          return false
        }
      }
    }
    prev = lst[i]
  }
  return true
}
```
