```js
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(num => (num - min) / (max - min));
}
```
