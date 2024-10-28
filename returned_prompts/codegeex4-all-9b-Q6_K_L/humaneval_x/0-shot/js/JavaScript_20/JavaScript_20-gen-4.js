```javascript
const findClosestElements = (numbers) => {
  const sortedNumbers = numbers.sort((a, b) => a - b);
  let minDiff = Infinity;
  let result = [];
  for (let i = 0; i < sortedNumbers.length - 1; i++) {
    const diff = sortedNumbers[i + 1] - sortedNumbers[i];
    if (diff < minDiff) {
      minDiff = diff;
      result = [sortedNumbers[i], sortedNumbers[i + 1]];
    }
  }
  return result;
}
```
