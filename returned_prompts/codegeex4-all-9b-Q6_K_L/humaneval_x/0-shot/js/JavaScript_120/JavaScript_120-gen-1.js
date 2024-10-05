```js
const maximum = (arr, k) => {
  if (k === 0) return [];
  let top = [...arr].sort((a, b) => b - a);
  return top.slice(0, k);
}
```