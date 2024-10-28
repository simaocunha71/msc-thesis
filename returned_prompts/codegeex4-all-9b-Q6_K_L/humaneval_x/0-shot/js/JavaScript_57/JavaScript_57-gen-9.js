```js
const monotonic = (l) => {
  if (l.length < 2) return true;
  const isIncreasing = l.every((x, i) => i === 0 || x >= l[i - 1]);
  const isDecreasing = l.every((x, i) => i === 0 || x <= l[i - 1]);
  return isIncreasing || isDecreasing;
}
```