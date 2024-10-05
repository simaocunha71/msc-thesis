```java
const sumSquares = (lst) => {
  let sum = 0
  for (let i = 0; i < lst.length; i++) {
    sum += Math.pow(Math.ceil(lst[i]), 2)
  }
  return sum
}
```