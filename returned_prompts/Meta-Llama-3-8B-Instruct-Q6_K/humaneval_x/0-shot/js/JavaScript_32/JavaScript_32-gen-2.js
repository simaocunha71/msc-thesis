Here is the solution in JavaScript:

```javascript
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

const findZero = (xs) => {
  if (xs.length % 2 !== 0) {
    throw new Error("xs must have even number of coefficients");
  }
  const n = xs.length / 2;
  const a = xs[n];
  const b = xs[n - 1];
  const c = xs[n - 2];
  const d = xs[0];
  return -b / (2 * a);
};
```
This code first checks if the number of coefficients is even. If not, it throws an error. Then it calculates the coefficients a, b, c, and d from the input list xs. Finally, it uses the quadratic formula to find the root of the polynomial. Note that this code assumes the largest non-zero coefficient is at the highest degree. If not, the quadratic formula will not work correctly.

The function `findZero` is designed to find the root of a quadratic polynomial. It takes a list of coefficients as input and returns the root of the polynomial. The coefficients are assumed to be in descending order of degree. The function first checks if the number of coefficients is even. If not, it throws an error. Then it calculates the coefficients a, b, and c from the input list. Finally, it uses the quadratic formula to find the root of the polynomial. The quadratic formula is `x = -b / (2 * a)`. This formula is used because the polynomial is a quadratic polynomial, which is of the form `ax^2 + bx + c`.

The function `poly` is a helper function that evaluates a polynomial at a given point. It takes a list of coefficients and a point as input and returns the value of the polynomial at that point. The function uses the reduce method to iterate over the coefficients and add them to the result. The index of the current coefficient is used to calculate the power of the point to which it should be raised.

The unit tests are:
```javascript
console.log(Math.round(findZero([1, 2]), 2)); // -0.5
console.log(Math.round(findZero([-6, 11, -6, 1]), 2)); // 1.0
```
These tests check if the function `findZero