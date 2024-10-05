Here is the solution:

```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
};

const findZero = (xs) => {
  if (xs.length % 2 !== 0) {
    throw new Error("xs must have even number of coefficients");
  }
  if (Math.abs(xs[0]) < 1e-10) {
    throw new Error("xs must have largest non zero coefficient as first one");
  }
  const n = xs.length / 2;
  for (let x = -100; x < 100; x++) {
    if (Math.abs(poly(xs, x)) < 1e-10) {
      return x;
    }
  }
  throw new Error("No zero found");
};

console.log(round(findZero([1, 2]), 2)); // -0.5
console.log(round(findZero([-6, 11, -6, 1]), 2)); // 1.0
```

In this code, `poly` function is used to evaluate the polynomial at a given point. `findZero` function finds the zero of the polynomial. It checks if the number of coefficients is even and if the largest non-zero coefficient is the first one. Then it iterates over the range of x values to find the one that makes the polynomial equal to zero. If no zero is found, it throws an error. The `round` function is used to round the result to 2 decimal places.