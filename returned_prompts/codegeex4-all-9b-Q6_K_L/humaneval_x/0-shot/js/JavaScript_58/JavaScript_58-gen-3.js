```js
const common = (l1, l2) => {
  return [...new Set(l1)].filter(x => l2.includes(x)).sort((a, b) => a - b);
}
```