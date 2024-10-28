```javascript
  let result = '';
  let maxUnique = 0;

  for (let word of words) {
    const uniqueChars = new Set(word).size;
    if (uniqueChars > maxUnique) {
      maxUnique = uniqueChars;
      result = word;
    } else if (uniqueChars === maxUnique) {
      result = result < word ? result : word;
    }
  }

  return result;
};
```