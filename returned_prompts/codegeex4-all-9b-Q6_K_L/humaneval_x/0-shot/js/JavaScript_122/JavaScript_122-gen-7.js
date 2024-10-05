```js
const addElements = (arr, k) => {
  if (k > arr.length) k = arr.length;
  return arr.slice(0, k).reduce((acc, el) => acc + (el < 100 ? el : 0), 0);
};
```
