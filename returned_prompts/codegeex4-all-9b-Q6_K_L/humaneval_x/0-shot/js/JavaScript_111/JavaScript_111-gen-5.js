```javascript
  const words = test.split(' ');
  const counts = {};
  words.forEach(word => {
    counts[word] = (counts[word] || 0) + 1;
  });
  const maxCount = Math.max(...Object.values(counts));
  const maxWords = Object.keys(counts).filter(key => counts[key] === maxCount);
  return maxWords.reduce((acc, word) => {
    acc[word] = maxCount;
    return acc;
  }, {});
};
```
