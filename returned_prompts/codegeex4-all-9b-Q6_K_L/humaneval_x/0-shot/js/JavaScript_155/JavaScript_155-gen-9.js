```java
const evenOddCount = (num) => {
  let evenCount = 0, oddCount = 0
  num = Math.abs(num)
  while (num > 0) {
    let digit = num % 10
    if (digit % 2 === 0) {
      evenCount++
    } else {
      oddCount++
    }
    num = Math.floor(num / 10)
  }
  return [evenCount, oddCount]
}
```
