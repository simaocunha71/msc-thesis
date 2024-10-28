```java
const isSorted = (lst) => {
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > lst[i + 1]) return false;
    if (lst[i] === lst[i + 1] && i > 0 && lst[i] === lst[i - 1]) return false;
  }
  return true;
}
```
