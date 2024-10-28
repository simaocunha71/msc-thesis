```javascript
const countDistinctCharacters = (string) => {
  let distinctChars = new Set();
  for (let char of string) {
    distinctChars.add(char.toLowerCase());
  }
  return distinctChars.size;
}
```