```js
const findMax = (words) => {
  let maxUniqueChars = 0;
  let maxUniqueWord = '';

  words.forEach(word => {
    const uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxUniqueWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxUniqueWord = word < maxUniqueWord ? word : maxUniqueWord;
    }
  });

  return maxUniqueWord;
};
```