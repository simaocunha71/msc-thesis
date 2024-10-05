```js
const circularShift = (x, shift) => {
  if (shift > x.toString().length) {
    return x.toString().split('').reverse().join('');
  } else {
    return x.toString().slice(-shift) + x.toString().slice(0, -shift);
  }
}
```
