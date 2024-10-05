```js
const rescaleToUnit = (numbers) => {
  if (numbers.length < 2) return numbers;
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
};
```