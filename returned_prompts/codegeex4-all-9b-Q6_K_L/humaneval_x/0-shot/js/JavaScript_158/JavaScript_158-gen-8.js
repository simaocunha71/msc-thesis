```javascript
const findMax = (words) => {
  let maxUnique = 0;
  let result = "";
  for (let word of words) {
    let uniqueChars = [...new Set(word.split("")).sort()];
    if (uniqueChars.length > maxUnique) {
      maxUnique = uniqueChars.length;
      result = word;
    } else if (uniqueChars.length === maxUnique) {
      if (word < result) {
        result = word;
      }
    }
  }
  return result;
};

console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb" ,"cc"])); // "aaaaaaa"
```