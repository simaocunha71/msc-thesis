```java
const solve = (N) => {
  let sum = 0
  while (N > 0) {
    sum += N % 2
    N = Math.floor(N / 2)
  }
  return sum.toString(2)
}
```