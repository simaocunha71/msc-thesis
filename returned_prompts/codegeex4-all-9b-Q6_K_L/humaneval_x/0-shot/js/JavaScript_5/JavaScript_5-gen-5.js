```js
const intersperse = (numbers, delimeter) => {
  var result = [];
  for (var i = 0; i < numbers.length; i++) {
    if (i > 0) result.push(delimeter);
    result.push(numbers[i]);
  }
  return result;
};
```