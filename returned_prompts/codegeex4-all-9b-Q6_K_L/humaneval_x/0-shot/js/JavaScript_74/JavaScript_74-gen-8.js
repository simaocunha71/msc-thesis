```java
const totalMatch = (lst1, lst2) => {
  let total1 = lst1.reduce((prev, item) => prev + item.length, 0);
  let total2 = lst2.reduce((prev, item) => prev + item.length, 0);
  if (total1 <= total2) {
    return lst1;
  } else {
    return lst2;
  }
}
```
