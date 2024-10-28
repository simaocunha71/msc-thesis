Here is a solution to the problem using the Newton-Raphson method for finding the root of a polynomial equation.

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
  let x = xs[1] / xs[0];
  let prev = 0;
  let curr = poly(xs, x);
  let epsilon = 1e-6;
  while (Math.abs(curr) > epsilon) {
    prev = x;
    x = x - curr / poly(xs.map((x, i) => i === 0 ? 1 : x * Math.pow(prev, i)), x);
    curr = poly(xs, x);
  }
  return x;
};
```

This code first checks if the input array `xs` has an even number of coefficients. If not, it throws an error. Then it initializes `x` to the value of the second coefficient divided by the first coefficient. This is a reasonable initial guess since the polynomial is a linear function for small values of `x`.

The Newton-Raphson method is then used to find the root of the polynomial. The method is an iterative process that starts with an initial guess `x` and repeatedly updates `x` as follows:

x_new = x_old - f(x_old) / f'(x_old)

where `f(x)` is the polynomial and `f'(x)` is its derivative. The derivative is computed by multiplying the polynomial by `x` and then taking the derivative.

The iteration stops when the absolute value of the polynomial at `x` is less than a small positive value `epsilon`. This value is set to `1e-6` in this code.

Finally, the code returns the root `x` of the polynomial. If the polynomial has multiple roots, this code will only return one of them. If you want to find all roots, you will need to modify the code to handle this case.