```javascript
  const wordWithMaxUniqueChars = words.reduce((maxWord, currentWord) => {
    const uniqueChars = new Set(currentWord.split(''));
    const uniqueCharCount = uniqueChars.size;
    const maxCharCount = new Set(maxWord.split('')).size;
    if (uniqueCharCount > maxCharCount) {
      return currentWord;
    } else if (uniqueCharCount === maxCharCount) {
      return maxWord < currentWord ? maxWord : currentWord;
    } else {
      return maxWord;
    }
  });

  return wordWithMaxUniqueChars;
};
```