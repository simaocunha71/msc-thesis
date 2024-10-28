To find the zero of a polynomial, we can use the Newton-Raphson method, which iteratively approximates the root of a function. The Newton-Raphson method works by starting with an initial guess for the root and then repeatedly refining the guess using the formula:

x_{n+1} = x_n - f(x_n) / f'(x_n)

where f(x) is the polynomial and f'(x) is its derivative.

Here's the implementation of the findZero function using the Newton-Raphson method:

```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const polyDerivative = (xs) => {
  return xs.map((item, index) => {
    return item * index;
  });
}

const findZero = (xs, initialGuess) => {
  let x = initialGuess;
  let fx = poly(xs, x);
  let fxPrime = polyDerivative(xs);

  while (Math.abs(fx) > 1e-6) {
    x = x - fx / fxPrime;
    fx = poly(xs, x);
    fxPrime = polyDerivative(xs);
  }

  return x;
}

console.log(round(findZero([1, 2]), 2)); // f(x) = 1 + 2x
console.log(round(findZero([-6, 11, -6, 1]), 2)); // (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This implementation starts with an initial guess of 0 and iteratively refines the guess until the absolute value of the function at the guess is less than 1e-6, which is a small threshold to determine if the guess is close enough to the actual root. The derivative of the polynomial is calculated using the polyDerivative function, which multiplies each coefficient by its index.

Note that this implementation assumes that the polynomial has an even number of coefficients and that the largest non-zero coefficient is the leading coefficient. If these assumptions are not met, the implementation may not find the correct root.