```java
const largestSmallestIntegers = (lst) => {
  let positive = null
  let negative = null
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > 0) {
      if (positive == null) positive = lst[i]
      else if (lst[i] < positive) positive = lst[i]
    } else if (lst[i] < 0) {
      if (negative == null) negative = lst[i]
      else if (lst[i] > negative) negative = lst[i]
    }
  }
  return [negative, positive]
}
```
