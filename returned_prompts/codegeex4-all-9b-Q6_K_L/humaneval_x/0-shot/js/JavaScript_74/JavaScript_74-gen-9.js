```java
const totalMatch = (lst1, lst2) => {
  var sum1 = lst1.map(x => x.length).reduce((a, c) => a + c, 0);
  var sum2 = lst2.map(x => x.length).reduce((a, c) => a + c, 0);
  if (sum1 <= sum2) { return lst1 }
  else { return lst2 }
}
```
