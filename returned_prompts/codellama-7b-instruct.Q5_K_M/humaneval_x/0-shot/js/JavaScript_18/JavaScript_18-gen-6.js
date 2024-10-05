
```js
const howManyTimes = (string, substring) => {
  let count = 0;
  let index = 0;
  while ((index = string.indexOf(substring, index)) !== -1) {
    index += substring.length;
    count++;
  }
  return count;
};
```
