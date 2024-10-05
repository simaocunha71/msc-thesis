```java
const compareOne = (a, b) => {
  if (a === b) return null
  let a_num = Number(a)
  let b_num = Number(b)
  if (isNaN(a_num) || isNaN(b_num)) return a_num > b_num ? a : b
  return a_num > b_num ? a_num : b_num
}
```
