```javascript
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;
  const firstKey = Object.keys(dict)[0];
  const isLower = firstKey === firstKey.toLowerCase();
  const isUpper = firstKey === firstKey.toUpperCase();
  return Object.keys(dict).every(key => isLower ? key === key.toLowerCase() : key === key.toUpperCase());
}
```