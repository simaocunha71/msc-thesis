```js
const maximum = (arr, k) => {
  // Sort the array in descending order
  arr.sort((a, b) => b - a);
  // Slice the first k elements
  return arr.slice(0, k);
}
```