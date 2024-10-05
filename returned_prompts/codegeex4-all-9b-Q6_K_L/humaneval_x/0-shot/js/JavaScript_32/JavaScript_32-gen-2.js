```js
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const findZero = (xs) => {
  let x = 0;
  let step = 1;
  while (Math.abs(poly(xs, x)) > 0.0001) {
    x += step;
    if (poly(xs, x) * poly(xs, x - step) < 0) {
      step = -step / 2;
    }
  }
  return x;
}
```