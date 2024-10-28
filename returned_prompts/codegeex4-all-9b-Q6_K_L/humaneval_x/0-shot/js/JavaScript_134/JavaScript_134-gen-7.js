```java
const checkIfLastCharIsALetter = (txt) => {
  let t = txt.split(' ')
  let lastWord = t[t.length - 1]
  let lastChar = lastWord[lastWord.length - 1]
  if (lastChar.match(/[a-z]/i) && lastChar !== ' ' && lastChar !== '.' && lastChar !== ',') {
    return true
  }
  return false
}
```
