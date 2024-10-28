```js
const uniqueDigits = (x) => {
  return x.filter(n => !String(n).includes('2') && !String(n).includes('4') && !String(n).includes('6') && !String(n).includes('8')).sort((a, b) => a - b);
}
```
