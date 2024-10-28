```javascript
const maximum = (arr, k) => {
  arr.sort((a, b) => b - a);
  return arr.slice(0, k);
};
```