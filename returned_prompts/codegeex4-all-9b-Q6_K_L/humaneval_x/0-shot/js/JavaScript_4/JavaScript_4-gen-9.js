```js
const meanAbsoluteDeviation = (numbers) => {
  const x_mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  const deviations = numbers.map((x) => Math.abs(x - x_mean));
  return deviations.reduce((a, b) => a + b, 0) / deviations.length;
}
```