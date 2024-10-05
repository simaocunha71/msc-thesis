```javascript
const rescaleToUnit = (numbers) => {
  // First, find the minimum and maximum values in the array
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  // Then, for each number in the array, subtract the minimum value and divide by the range
  return numbers.map(num => (num - min) / (max - min));
}
```
