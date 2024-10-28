```js
const unique = (l) => {
  return [...new Set(l)].sort((a, b) => a - b);
}
```