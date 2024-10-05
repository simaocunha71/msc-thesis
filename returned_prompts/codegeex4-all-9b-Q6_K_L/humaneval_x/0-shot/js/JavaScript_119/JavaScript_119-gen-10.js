```java
const matchParens = (lst) => {
  const s1 = lst[0]
  const s2 = lst[1]
  const count1 = s1.split('(').length - 1
  const count2 = s2.split('(').length - 1
  const count3 = s1.split(')').length - 1
  const count4 = s2.split(')').length - 1
  if (count1 == count2 && count3 == count4) {
    return 'Yes'
  } else {
    return 'No'
  }
}
```
