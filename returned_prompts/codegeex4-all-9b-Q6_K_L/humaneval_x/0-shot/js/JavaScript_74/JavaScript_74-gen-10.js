```java
const totalMatch = (lst1, lst2) => {
  if (lst1.length === 0 && lst2.length === 0) { return lst1; }
  let sum1 = lst1.reduce((prev, item) => prev + item.length, 0);
  let sum2 = lst2.reduce((prev, item) => prev + item.length, 0);
  if (sum1 <= sum2) { return lst1; }
  return lst2;
}
```
