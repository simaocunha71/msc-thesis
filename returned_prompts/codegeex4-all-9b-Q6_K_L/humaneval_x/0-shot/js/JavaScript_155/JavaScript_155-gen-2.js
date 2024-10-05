```java
const evenOddCount = (num) => {
  let numStr = Math.abs(num).toString()
  let evenCount = 0
  let oddCount = 0
  for (let i = 0; i < numStr.length; i++) {
    if (parseInt(numStr[i]) % 2 === 0) {
      evenCount++
    } else {
      oddCount++
    }
  }
  return [evenCount, oddCount]
}
```
