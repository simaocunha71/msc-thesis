```js
const uniqueDigits = (x) => {
  return x.filter(el => {
    return el.toString().split('').every(digit => digit % 2 !== 0);
  }).sort((a, b) => a - b);
}
```