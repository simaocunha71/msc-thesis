```js
const changeBase = (x, base) => {
  if (x < base) {
    return x.toString();
  }
  const quotient = Math.floor(x / base);
  const remainder = x % base;
  return changeBase(quotient, base) + remainder.toString();
};
```