```js
const hasCloseElements = (numbers, threshold) => {
  if (numbers.length < 2) {
    return false;
  }
  numbers.sort((a, b) => a - b);
  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i + 1] - numbers[i] < threshold) {
      return true;
    }
  }
  return false;
}
```