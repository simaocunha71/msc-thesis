```java
const howManyTimes = (string, substring) => {
  let ret = 0
  for (let i = 0; i <= string.length - substring.length; i++) {
    if (string.substring(i, i + substring.length) == substring) {
      ret++
    }
  }
  return ret
}
```
