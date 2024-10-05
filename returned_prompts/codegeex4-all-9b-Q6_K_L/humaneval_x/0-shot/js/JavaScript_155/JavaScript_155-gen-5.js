```java
const evenOddCount = (num) => {
  let countOdd = 0
  let countEven = 0
  let str = Math.abs(num).toString()
  for (let i = 0; i < str.length; i++) {
    let digit = parseInt(str[i])
    if (digit % 2 === 0) {
      countEven++
    } else {
      countOdd++
    }
  }
  return [countEven, countOdd]
}
```
