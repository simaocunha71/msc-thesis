```js
const greatestCommonDivisor = (a, b) => {
  let remainder;
  while (b) {
    remainder = a % b;
    a = b;
    b = remainder;
  }
  return a;
}
```
