```javascript
const changeBase = (x, base) => {
  const digits = '0123456789abcdefghijklmnopqrstuvwxyz';
  let result = '';
  while (x > 0) {
    result = digits[x % base] + result;
    x = Math.floor(x / base);
  }
  return result;
};
```