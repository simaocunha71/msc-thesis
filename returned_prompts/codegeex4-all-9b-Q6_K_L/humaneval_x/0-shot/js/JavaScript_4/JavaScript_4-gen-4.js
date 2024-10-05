```javascript
const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  return numbers.reduce((a, b) => a + Math.abs(b - mean), 0) / numbers.length;
}
```