```java
const howManyTimes = (string, substring) => {
  let count = 0
  for (let i = 0; i < string.length; i++) {
    if (string.slice(i, i + substring.length) === substring) {
      count++
      i += substring.length - 1
    }
  }
  return count
}
```
