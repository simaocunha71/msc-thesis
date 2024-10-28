```js
const findMax = (words) => {
  let max = 0;
  let result = "";
  for (let i = 0; i < words.length; i++) {
    let uniqueChars = new Set(words[i]).size;
    if (uniqueChars > max) {
      max = uniqueChars;
      result = words[i];
    } else if (uniqueChars === max) {
      result = words[i].localeCompare(result) < 0 ? words[i] : result;
    }
  }
  return result;
}
```