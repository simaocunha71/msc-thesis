```java
const totalMatch = (lst1, lst2) => {
  if (lst1.length === 0 && lst2.length === 0) { return [] }
  let sum1 = 0
  let sum2 = 0
  for (let i = 0; i < lst1.length; i++) {
    sum1 += lst1[i].length
  }
  for (let i = 0; i < lst2.length; i++) {
    sum2 += lst2[i].length
  }
  if (sum1 < sum2) { return lst1 }
  if (sum2 < sum1) { return lst2 }
  return lst1
}
```
