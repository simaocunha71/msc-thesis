```js
const meanAbsoluteDeviation = (numbers) => {
  if (numbers.length === 0) return 0;

  const mean = numbers.reduce((acc, val) => acc + val, 0) / numbers.length;
  const deviations = numbers.map((num) => Math.abs(num - mean));
  const mad = deviations.reduce((acc, val) => acc + val, 0) / deviations.length;

  return mad;
};
```
