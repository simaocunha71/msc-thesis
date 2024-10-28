```js
const rescaleToUnit = (numbers) => {
  const minVal = Math.min(...numbers);
  const maxVal = Math.max(...numbers);
  return numbers.map(num => (num - minVal) / (maxVal - minVal));
}
```