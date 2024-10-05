```javascript
const findMax = (words) => {
  if (words.length === 0) return "";
  let maxUniqueCount = 0;
  let maxUniqueWord = "";
  for (let word of words) {
    const uniqueChars = new Set(word.split(""));
    if (uniqueChars.size > maxUniqueCount) {
      maxUniqueCount = uniqueChars.size;
      maxUniqueWord = word;
    } else if (uniqueChars.size === maxUniqueCount && word < maxUniqueWord) {
      maxUniqueWord = word;
    }
  }
  return maxUniqueWord;
}
```