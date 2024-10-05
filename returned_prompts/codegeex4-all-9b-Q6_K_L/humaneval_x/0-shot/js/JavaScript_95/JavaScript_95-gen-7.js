```js
const checkDictCase = (dict) => {
  let keys = Object.keys(dict);
  if (keys.length === 0) {
    return false;
  }
  const firstKey = keys[0];
  if (typeof firstKey !== 'string') {
    return false;
  }
  const isLowerCase = firstKey === firstKey.toLowerCase();
  return keys.every(key => typeof key === 'string' && (isLowerCase ? key === key.toLowerCase() : key === key.toUpperCase()));
}
```
