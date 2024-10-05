```javascript
const checkDictCase = (dict) => {
  const isLower = (str) => str === str.toLowerCase();
  const isUpper = (str) => str === str.toUpperCase();
  const isString = (val) => typeof val === 'string';
  const allLower = Object.keys(dict).every(isLower);
  const allUpper = Object.keys(dict).every(isUpper);
  const allString = Object.values(dict).every(isString);
  return (allLower || allUpper) && allString;
}
```