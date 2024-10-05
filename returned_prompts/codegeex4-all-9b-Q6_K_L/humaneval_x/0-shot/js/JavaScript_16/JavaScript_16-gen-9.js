```javascript
const countDistinctCharacters = (string) => {
  const chars = new Set(string.toLowerCase().split(''));
  return chars.size;
};
```
