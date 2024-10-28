```js
const derivative = (xs) => {
  return xs.map((coefficient, index) => coefficient * index);
};
```

This function takes an array of coefficients `xs` and returns a new array representing the derivative of the polynomial. The derivative of a polynomial `xs[0] + xs[1] * x + xs[2] * x^2 + ....` is obtained by multiplying each coefficient by its corresponding index.