```js
const prodSigns = (arr) => {
  if (arr.length == 0) return null;
  let product = arr.reduce((acc, val) => acc * val, 1);
  let sum = arr.reduce((acc, val) => acc + Math.abs(val), 0);
  let sign = product >= 0 ? 1 : -1;
  return sum * sign;
}
```