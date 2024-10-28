```javascript
const digits = (n) => {
  return Math.floor(n / 1000) * 7 + Math.floor((n / 100) % 10) * 3 + Math.floor((n / 10) % 10) * 1 + n % 10 * 0;
}
```
