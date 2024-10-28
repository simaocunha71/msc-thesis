```java
const totalMatch = (lst1, lst2) => {
  let l1 = 0
  let l2 = 0
  for (let i = 0; i < lst1.length; i++) {
    l1 += lst1[i].length
  }
  for (let i = 0; i < lst2.length; i++) {
    l2 += lst2[i].length
  }
  if (l1 <= l2) {
    return lst1
  } else {
    return lst2
  }
}
```
