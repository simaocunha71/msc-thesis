```js
const maximum = (arr, k) => {
  if (k === 0) return [];
  arr.sort((a, b) => b - a);
  return arr.slice(0, k);
};
```