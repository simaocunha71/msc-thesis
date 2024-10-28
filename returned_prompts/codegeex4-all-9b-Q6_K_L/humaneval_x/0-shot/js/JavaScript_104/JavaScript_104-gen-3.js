```js
const uniqueDigits = (x) => {
  return x.filter(num => {
    return String(num).split('').every(digit => digit % 2 !== 0);
  }).sort((a, b) => a - b);
}
```
