```javascript
const sumProduct = (numbers, int = 1) => {
  if (numbers.length === 0) {
    return [0, 1];
  }

  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }

  return [sum, numbers.reduce((a, b) => a * b, int)];
};
```
