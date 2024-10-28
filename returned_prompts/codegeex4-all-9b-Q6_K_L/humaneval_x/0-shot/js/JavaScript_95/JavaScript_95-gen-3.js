```js
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;

  const isAllLowerCase = Object.keys(dict).every(key => key === key.toLowerCase());
  const isAllUpperCase = Object.keys(dict).every(key => key === key.toUpperCase());

  return isAllLowerCase || isAllUpperCase;
}
```