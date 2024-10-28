```js
const monotonic = (l) => {
  if (l.length < 2) return true;
  const isIncreasing = l.every((num, i) => i === 0 || num >= l[i - 1]);
  const isDecreasing = l.every((num, i) => i === 0 || num <= l[i - 1]);
  return isIncreasing || isDecreasing;
}
```
