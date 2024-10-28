```js
const unique = (l) => {
  return Array.from(new Set(l)).sort((a, b) => a - b);
}
```