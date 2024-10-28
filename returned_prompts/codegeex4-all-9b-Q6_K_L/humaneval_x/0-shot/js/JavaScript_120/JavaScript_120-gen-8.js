```javascript
const maximum = (arr, k) => {
  if (k === 0) {
    return [];
  }
  if (arr.length <= k) {
    return arr.sort((a, b) => b - a);
  }
  return arr.sort((a, b) => b - a).slice(0, k);
}
```