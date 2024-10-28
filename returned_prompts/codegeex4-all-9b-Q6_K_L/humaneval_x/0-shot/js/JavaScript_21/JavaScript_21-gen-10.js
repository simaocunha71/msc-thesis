```js
const rescaleToUnit = (numbers) => {
  if (numbers.length < 2) {
    throw new Error("At least two numbers are required");
  }
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(num => (num - min) / (max - min));
}
```
