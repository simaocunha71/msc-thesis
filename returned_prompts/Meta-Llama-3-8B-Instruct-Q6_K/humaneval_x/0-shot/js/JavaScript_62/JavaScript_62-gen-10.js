```
return xs.slice(1).map((x, i) => i * x)
```
Explanation:
The `derivative` function takes an array `xs` representing the coefficients of a polynomial. The derivative of a polynomial is a new polynomial whose coefficients are the derivatives of the original polynomial's coefficients.

The `slice(1)` method is used to get a new array that excludes the first element of the original array. This is because the derivative of the constant term is zero.

The `map` method is used to apply a transformation to each element of the new array. The transformation is `i * x`, where `i` is the index of the element and `x` is the element itself. This is because the derivative of a term `x^n` is `n * x^(n-1)`.

The resulting array is then returned as the derivative of the original polynomial. For example, if the input is `[3, 1, 2, 4, 5]`, the output will be `[1, 4, 12, 20]`, which are the derivatives of the terms `3`, `x`, `x^2`, and `x^3` respectively.