```javascript
const findClosestElements = (numbers) => {
  let minDiff = Infinity;
  let pair = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < minDiff) {
        minDiff = diff;
        pair = [numbers[i], numbers[j]];
      }
    }
  }

  return pair.sort((a, b) => a - b);
}
```
