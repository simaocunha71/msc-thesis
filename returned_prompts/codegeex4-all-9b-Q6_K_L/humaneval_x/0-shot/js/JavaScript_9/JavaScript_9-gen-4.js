```js
const rollingMax = (numbers) => {
  const result = [];
  let max = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    result.push(max);
  }

  return result;
}
```