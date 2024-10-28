```javascript
const splitWords = (txt) => {
  let words = txt.split(" ")
  if (words.length > 1) {
    return words
  }
  words = txt.split(",")
  if (words.length > 1) {
    return words
  }
  let count = 0
  for (let i = 0; i < txt.length; i++) {
    if (txt[i] === txt[i].toLowerCase() && txt[i].charCodeAt(0) % 2 === 1) {
      count++
    }
  }
  return count
}
```
