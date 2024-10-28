```js
const rollingMax = (numbers) => {
  if (numbers.length === 0) return [];
  let max = numbers[0];
  let result = [max];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    result.push(max);
  }
  return result;
};
```
