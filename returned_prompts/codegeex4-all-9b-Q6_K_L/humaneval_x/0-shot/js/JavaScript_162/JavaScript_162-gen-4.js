```javascript
const stringToMd5 = (text) => {
  if (text === '') return null;
  return md5(text);
};
```