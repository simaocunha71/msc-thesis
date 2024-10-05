```java
const checkIfLastCharIsALetter = (txt) => {
  if (txt.length === 0) return false
  let lastChar = txt[txt.length - 1]
  return /[a-zA-Z]$/.test(lastChar) && !/\w/.test(lastChar)
}
```
