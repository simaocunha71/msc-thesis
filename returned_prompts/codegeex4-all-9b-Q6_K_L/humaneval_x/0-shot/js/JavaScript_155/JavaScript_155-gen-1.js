```java
const evenOddCount = (num) => {
  var even = 0, odd = 0
  num = Math.abs(num).toString().split('')
  num.forEach(x => {
    if (x % 2 == 0) even++
    else odd++
  })
  return [even, odd]
}
```