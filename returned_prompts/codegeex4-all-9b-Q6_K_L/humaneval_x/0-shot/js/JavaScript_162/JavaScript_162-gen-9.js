```js
const stringToMd5 = (text) => {
  return text.length === 0 ? null : md5(text);
};
```
