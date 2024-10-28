```js
const derivative = (xs) => {
  // Return the derivative of the polynomial represented by xs
  return xs.slice(1).map((x, i) => x * (i + 1));
};
```
