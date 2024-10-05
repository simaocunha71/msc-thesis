```js
const sortArray = (array) => {
  let sum = array[0] + array[array.length - 1];
  return array.slice().sort(sum % 2 === 0 ? (a, b) => b - a : (a, b) => a - b);
}
```