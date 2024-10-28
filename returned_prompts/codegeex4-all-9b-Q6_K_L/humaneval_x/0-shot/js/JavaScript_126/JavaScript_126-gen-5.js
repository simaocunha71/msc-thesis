```java
const isSorted = (lst) => {
  for (let i = 1; i < lst.length; i++) {
    if (lst[i - 1] > lst[i]) {
      return false;
    }
    if (lst[i - 1] == lst[i]) {
      if (lst[i] == lst[i + 1]) {
        return false;
      }
    }
  }
  return true;
}
```
