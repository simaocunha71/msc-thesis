```js
const stringToMd5 = (text) => {
  if (text === '') return null;
  return CryptoJS.MD5(text).toString();
};
```