```js
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;
  const firstKey = Object.keys(dict)[0];
  return (firstKey === firstKey.toLowerCase() && firstKey === firstKey.toUpperCase()) 
    ? false 
    : firstKey === firstKey.toLowerCase() === Object.keys(dict).every(key => key === key.toLowerCase()) 
      || firstKey === firstKey.toUpperCase() === Object.keys(dict).every(key => key === key.toUpperCase());
};
```