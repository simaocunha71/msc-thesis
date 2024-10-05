```javascript
const findClosestElements = (numbers) => {
  numbers.sort((a, b) => a - b);
  let minDiff = Infinity;
  let closestPair = [numbers[0], numbers[1]];
  for (let i = 0; i < numbers.length - 1; i++) {
    const diff = numbers[i + 1] - numbers[i];
    if (diff < minDiff) {
      minDiff = diff;
      closestPair = [numbers[i], numbers[i + 1]];
    }
  }
  return closestPair;
}
```
