```js
const concatenate = (strings) => {
  if (strings.length === 0) return '';
  return strings.reduce((acc, string) => acc + string, '');
}
```