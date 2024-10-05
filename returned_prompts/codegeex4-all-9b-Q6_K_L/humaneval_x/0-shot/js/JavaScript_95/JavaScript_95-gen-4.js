```javascript
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;
  const isLower = (str) => str === str.toLowerCase();
  const isUpper = (str) => str === str.toUpperCase();
  const allLowerCase = Object.keys(dict).every(isLower);
  const allUpperCase = Object.keys(dict).every(isUpper);
  return allLowerCase || allUpperCase;
}
```