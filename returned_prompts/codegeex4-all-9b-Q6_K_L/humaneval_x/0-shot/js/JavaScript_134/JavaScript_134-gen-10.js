```java
const checkIfLastCharIsALetter = (txt) => {
  let last = txt[txt.length - 1]
  if (last == ' ' || last == '' || !isNaN(last)) {
    return false
  }
  return true
}
```
