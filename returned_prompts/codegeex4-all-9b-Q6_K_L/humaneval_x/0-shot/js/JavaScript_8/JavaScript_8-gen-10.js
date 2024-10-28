```js
const sumProduct = (numbers, int = 1) => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    int *= numbers[i];
  }
  return [sum, int];
}
```
