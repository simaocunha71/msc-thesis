```java
const checkIfLastCharIsALetter = (txt) => {
  if (txt == '') return false
  let lastChar = txt[txt.length - 1];
  return (lastChar.match(/[a-z]/i) && !lastChar.match(/\w/))
}
```
