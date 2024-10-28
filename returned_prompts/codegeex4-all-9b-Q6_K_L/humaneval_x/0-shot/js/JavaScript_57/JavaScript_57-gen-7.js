```js
const monotonic = (l) => {
  const increasing = l.every((x, i) => i === 0 || x >= l[i - 1]);
  const decreasing = l.every((x, i) => i === 0 || x <= l[i - 1]);
  return increasing || decreasing;
};
```
