Here is the implementation of the findZero function in JavaScript. It uses the Newton-Raphson method to find the root of the polynomial. The Newton-Raphson method is a root-finding algorithm that iteratively updates an estimate for a root of a function F(x) until convergence is reached.

```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const findZero = (xs) => {
  // check if xs has even number of coefficients
  if (xs.length % 2 !== 0) {
    throw new Error('xs must have even number of coefficients');
  }

  // find the largest non-zero coefficient
  const maxIndex = xs.reduce((maxIndex, item, index) => {
    return item !== 0 ? index : maxIndex;
  }, null);

  // initialize x0 to the largest non-zero coefficient
  const x0 = maxIndex;

  // iterate until convergence
  for (let i = 0; i < 100; i++) { // max 100 iterations
    const f0 = poly(xs, x0);
    const f1 = poly(xs.map((item, index) => index * item), x0);

    if (Math.abs(f0) < 1e-6) {
      return x0;
    }

    x0 = x0 - f0 / f1;
  }

  throw new Error('Failed to find zero');
};
```

You can use this function to find the zero of a polynomial as follows:

```javascript
console.log(round(findZero([1, 2]), 2)); // f(x) = 1 + 2x
console.log(round(findZero([-6, 11, -6, 1]), 2)); // (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```


This implementation assumes that the polynomial has at least one real root. In practice, you may want to add more checks and error handling. For example, you could check if the polynomial has any complex roots, or if the Newton-Raphson method fails to converge. You could also use other root-finding algorithms, such as the bisection method or the secant method.