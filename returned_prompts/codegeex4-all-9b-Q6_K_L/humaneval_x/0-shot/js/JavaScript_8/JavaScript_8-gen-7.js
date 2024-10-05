```java
const sumProduct = (numbers, int) => {
  return numbers.reduce((acc, val) => [acc[0] + val, acc[1] * val], [0, 1])
}
```
