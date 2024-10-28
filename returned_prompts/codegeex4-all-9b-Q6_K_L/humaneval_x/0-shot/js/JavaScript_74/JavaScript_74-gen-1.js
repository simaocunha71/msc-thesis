```java
const totalMatch = (lst1, lst2) => {
  var l1 = lst1.reduce((prev, item) => prev + item.length, 0);
  var l2 = lst2.reduce((prev, item) => prev + item.length, 0);
  if (l1 <= l2) { return lst1 }
  if (l2 < l1) { return lst2 }
}
```
