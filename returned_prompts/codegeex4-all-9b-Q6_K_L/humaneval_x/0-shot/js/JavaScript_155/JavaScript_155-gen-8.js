```java
const evenOddCount = (num) => {
  var even = 0
  var odd = 0
  var arr = String(Math.abs(num)).split('')
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      even++
    } else {
      odd++
    }
  }
  return [even, odd]
}
```
