```js
const monotonic = (l) => {
  const increasing = l.every((val, i, arr) => i === 0 || val >= arr[i - 1]);
  const decreasing = l.every((val, i, arr) => i === 0 || val <= arr[i - 1]);
  return increasing || decreasing;
}
```