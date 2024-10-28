```js
const rollingMax = (numbers) => {
  let currentMax = numbers[0];
  return numbers.map((num, i) => {
    if (num > currentMax) {
      currentMax = num;
    }
    return currentMax;
  });
}
```
