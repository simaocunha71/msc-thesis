```js
const findMax = (words) => {
  const uniqueChars = (word) => new Set(word).size;
  let maxWord = words[0];
  let maxUniqueChars = uniqueChars(words[0]);
  for (let i = 1; i < words.length; i++) {
    const currUniqueChars = uniqueChars(words[i]);
    if (currUniqueChars > maxUniqueChars || (currUniqueChars === maxUniqueChars && words[i] < maxWord)) {
      maxWord = words[i];
      maxUniqueChars = currUniqueChars;
    }
  }
  return maxWord;
};
```
