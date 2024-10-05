```js
const compareOne = (a, b) => {
  if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b.replace(',', '.'));
  }
  if (a === b) return null;
  return a > b ? a : b;
}
```
