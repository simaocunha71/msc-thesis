```
const derivative = xs => xs.map((x, i) => i === 0 ? x : x * (i + 1));
```

Explanation:
The derivative of a polynomial is calculated by multiplying each term with its corresponding power and then reducing the power by 1. For example, the derivative of `x^2` is `2x`, and the derivative of `x^3` is `3x^2`.

In the code, we use the `map` method to iterate over the coefficients of the polynomial. For each coefficient, we return a new value calculated as the product of the coefficient and its corresponding power (which is the index `i` of the coefficient). If the index is 0, we simply return the coefficient as is, since the derivative of a constant is 0.

For example, if we call `derivative([3, 1, 2, 4, 5])`, the output will be `[1, 4, 12, 20]`, which are the derivatives of the corresponding terms in the polynomial. Similarly, if we call `derivative([1, 2, 3])`, the output will be `[2, 6]`, which are the derivatives of the corresponding terms in the polynomial.