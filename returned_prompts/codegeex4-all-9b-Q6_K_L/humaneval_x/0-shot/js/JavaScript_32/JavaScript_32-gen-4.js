```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const findZero = (xs) => {
  let a = xs[0];
  let b = xs[1];
  let x = b / a;
  let i = 2;
  while (Math.abs(poly(xs, x)) > 1e-10) {
    x = x - poly(xs, x) / (poly(xs, x + 1e-10) - poly(xs, x - 1e-10));
    i++;
  }
  return x;
}
```