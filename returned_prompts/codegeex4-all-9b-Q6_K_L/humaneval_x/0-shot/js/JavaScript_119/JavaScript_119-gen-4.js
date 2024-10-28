```java
const matchParens = (lst) => {
  let cnt1 = 0, cnt2 = 0
  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] == '(') cnt1++
    else cnt1--
  }
  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] == ')') cnt2++
    else cnt2--
  }
  return cnt1 == cnt2 ? 'Yes' : 'No'
}
```
