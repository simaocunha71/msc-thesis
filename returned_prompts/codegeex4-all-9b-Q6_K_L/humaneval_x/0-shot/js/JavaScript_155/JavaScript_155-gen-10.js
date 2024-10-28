```java
const evenOddCount = (num) => {
  var digits = Math.abs(num).toString().split("")
  var evenCount = 0
  var oddCount = 0
  for (let i = 0; i < digits.length; i++) {
    if (digits[i] % 2 == 0) {
      evenCount++
    } else {
      oddCount++
    }
  }
  return [evenCount, oddCount]
}
```
