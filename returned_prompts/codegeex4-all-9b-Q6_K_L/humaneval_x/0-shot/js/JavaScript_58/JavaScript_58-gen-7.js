```js
const common = (l1, l2) => {
  return [...new Set(l1.filter(item => l2.includes(item)))].sort((a, b) => a - b);
}
```