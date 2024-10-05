```javascript
const uniqueDigits = (x) => {
  return x.filter(y => {
    return y.toString().split('').every(z => {
      return z % 2 !== 0;
    });
  }).sort((a, b) => a - b);
}
```