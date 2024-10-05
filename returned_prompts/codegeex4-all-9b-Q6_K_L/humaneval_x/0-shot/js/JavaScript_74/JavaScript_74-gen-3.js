```java
const totalMatch = (lst1, lst2) => {
  var sum1 = lst1.reduce((prev, item) => prev + item.length, 0);
  var sum2 = lst2.reduce((prev, item) => prev + item.length, 0);
  if (sum1 <= sum2)
    return lst1;
  else
    return lst2;
}
```
