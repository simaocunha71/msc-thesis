```javascript
const allPrefixes = (string) => {
  let result = [];
  for (let i = 1; i <= string.length; i++) {
    result.push(string.slice(0, i));
  }
  return result;
}
```
