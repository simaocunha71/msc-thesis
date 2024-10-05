```javascript
const specialFactorial = (n) => {
  if (n <= 1) return 1;
  return n * specialFactorial(n-1);
}
```
