Here is the solution:

```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const findZero = (xs) => {
  if (xs.length % 2 !== 0) {
    throw new Error('xs must have even number of coefficients');
  }
  const n = xs.length / 2;
  const a = xs[n - 1];
  const b = xs[n];
  const c = xs[n + 1];
  const d = xs[n + 2];
  const discr = Math.pow(b, 2) - 4 * a * c;
  const sqrt = Math.sqrt(discr);
  const x1 = (-b + sqrt) / (2 * a);
  const x2 = (-b - sqrt) / (2 * a);
  if (Math.abs(c) > 0.0001) {
    return x1;
  } else {
    return x2;
  }
};
```

In the `findZero` function, we first check if the number of coefficients is even. If not, we throw an error. Then we calculate the coefficients of the polynomial. We calculate the discriminant of the quadratic equation, and use it to find the roots. If the polynomial is of degree 3 or higher, we return the root with the largest absolute value. If the polynomial is of degree 2, we return the other root.

Note that the `findZero` function assumes that the largest non-zero coefficient is at the highest power of x, which means that the polynomial is written in descending powers of x. If the polynomial is written in ascending powers of x, you would need to reverse the coefficients array before calling `findZero`. Also, the function returns a single root, even if there are multiple roots. If you want to find all roots, you would need to modify the function to find all the roots of the polynomial.