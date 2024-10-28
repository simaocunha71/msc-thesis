```java
const isSorted = (lst) => {
  let prev = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < prev) {
      return false;
    }
    prev = lst[i];
    if (lst[i] === prev && lst[i - 1] === prev) {
      return false;
    }
  }
  return true;
}
```
