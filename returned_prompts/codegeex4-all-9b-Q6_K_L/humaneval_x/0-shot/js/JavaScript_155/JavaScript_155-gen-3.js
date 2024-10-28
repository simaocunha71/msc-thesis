```java
const evenOddCount = (num) => {
  let even = 0, odd = 0
  if (num < 0) num = -num
  while (num > 0) {
    let digit = num % 10
    if (digit % 2 === 0) even++
    else odd++
    num = (num - digit) / 10
  }
  return [even, odd]
}
```
