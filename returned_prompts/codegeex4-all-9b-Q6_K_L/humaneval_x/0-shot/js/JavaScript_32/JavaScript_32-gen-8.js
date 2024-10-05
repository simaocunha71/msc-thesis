```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const findZero = (xs) => {
  let a = xs[0], b = xs[1];
  let x = -b / a;
  let f = poly(xs, x);
  let df = poly(xs.slice(1), x);
  if (Math.abs(f) < 1e-6) return x;
  let n = Math.floor(Math.log2(Math.abs(f))) - 1;
  let h = Math.pow(2, n);
  while (h > 1e-6) {
    let x1 = x - h * f / df;
    let f1 = poly(xs, x1);
    let df1 = poly(xs.slice(1), x1);
    if (Math.abs(f1) < Math.abs(f)) {
      x = x1;
      f = f1;
      df = df1;
    }
    h /= 2;
  }
  return x;
}
```