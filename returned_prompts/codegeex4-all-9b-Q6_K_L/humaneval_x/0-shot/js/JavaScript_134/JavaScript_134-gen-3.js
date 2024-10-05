```java
const checkIfLastCharIsALetter = (txt) => {
  let t = txt.trim()
  return t && /[a-z]/i.test(t[t.length - 1]) && t[t.length - 1] != ' '
}
```
