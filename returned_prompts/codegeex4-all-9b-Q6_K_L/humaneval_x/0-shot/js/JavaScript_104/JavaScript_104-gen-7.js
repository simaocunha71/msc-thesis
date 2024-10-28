```js
const uniqueDigits = (x) => {
  return x.filter(n => {
    const str = String(n);
    return !str.includes('2') && !str.includes('4') && !str.includes('6') && !str.includes('8');
  }).sort((a, b) => a - b);
}
```
