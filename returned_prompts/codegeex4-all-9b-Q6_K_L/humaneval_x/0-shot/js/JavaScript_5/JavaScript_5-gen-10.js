```js
const intersperse = (numbers, delimeter) => {
  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push(numbers[i]);
    if (i < numbers.length - 1) {
      result.push(delimeter);
    }
  }
  return result;
}
```