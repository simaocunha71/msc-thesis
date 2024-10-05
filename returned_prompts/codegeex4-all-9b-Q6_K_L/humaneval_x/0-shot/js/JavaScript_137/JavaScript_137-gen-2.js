```java
const compareOne = (a, b) => {
  let a_num = Number(a)
  let b_num = Number(b)
  if (a_num == b_num) return null
  if (a_num > b_num) return a
  return b
}
```