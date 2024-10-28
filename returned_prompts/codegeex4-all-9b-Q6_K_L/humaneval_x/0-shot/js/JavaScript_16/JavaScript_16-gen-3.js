```javascript
const countDistinctCharacters = (string) => {
  const lowerCaseString = string.toLowerCase();
  const uniqueCharacters = new Set(lowerCaseString);
  return uniqueCharacters.size;
}
```