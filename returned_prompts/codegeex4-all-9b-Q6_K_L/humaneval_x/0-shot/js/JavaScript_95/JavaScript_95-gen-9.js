```js
const checkDictCase = (dict) => {
  if(Object.keys(dict).length === 0) return false;
  const check = Object.keys(dict).every(key => typeof key === 'string');
  if(!check) return false;
  const firstChar = Object.keys(dict)[0][0];
  const isUpperCase = firstChar === firstChar.toUpperCase();
  return Object.keys(dict).every(key => (isUpperCase ? key[0] === firstChar.toUpperCase() : key[0] === firstChar.toLowerCase()));
};
```
