```js
const countDistinctCharacters = (string) => {
  const lowerCaseString = string.toLowerCase();
  return new Set(lowerCaseString).size;
}
```
