```javascript
const hasCloseElements = (numbers, threshold) => {
  let hasClose = false;
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (Math.abs(numbers[i] - numbers[j]) < threshold) {
        hasClose = true;
        break;
      }
    }
    if (hasClose) {
      break;
    }
  }
  return hasClose;
}
```