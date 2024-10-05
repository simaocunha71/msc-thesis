```java
const solution = (lst) => {
  let sum = 0
  for (let i = 0; i < lst.length; i += 2) {
    if (lst[i] % 2 === 1) {
      sum += lst[i]
    }
  }
  return sum
}
```
