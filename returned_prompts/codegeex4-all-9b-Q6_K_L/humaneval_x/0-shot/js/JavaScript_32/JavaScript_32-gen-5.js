The `findZero` function is using a numerical method to find the zero of a polynomial. However, the problem statement says that the function should only find one zero, even if there are many. This is not a correct implementation of the `findZero` function, as it will always return the first zero it finds, even if there are other zeros in the polynomial.

Here is the correct implementation of the `findZero` function:

```javascript
const findZero = (xs) => {
  const EPSILON = 0.00001;
  let left = -10000;
  let right = 10000;
  let mid = (left + right) / 2;
  let fmid = poly(xs, mid);

  while (Math.abs(fmid) > EPSILON) {
    if (fmid < 0) {
      left = mid;
    } else {
      right = mid;
    }
    mid = (left + right) / 2;
    fmid = poly(xs, mid);
  }

  return mid;
}
```

This implementation uses the bisection method to find the zero of the polynomial. It starts with a range of -10000 to 10000 and repeatedly halves the range until the absolute value of the polynomial at the midpoint is less than a small epsilon value. The midpoint is then returned as the zero of the polynomial.