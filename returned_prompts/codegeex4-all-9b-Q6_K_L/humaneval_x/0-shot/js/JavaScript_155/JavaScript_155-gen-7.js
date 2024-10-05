```java
const evenOddCount = (num) => {
  let arr = (num + '').split('')
  let evens = arr.filter(e => e % 2 === 0)
  let odds = arr.filter(e => e % 2 !== 0)
  return [evens.length, odds.length]
}
```
