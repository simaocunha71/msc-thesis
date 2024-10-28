```js
const digitSum = (s) => {
  return s.toUpperCase()
    .split('')
    .reduce((prev, item) => prev + item.charCodeAt(0), 0);
}
```