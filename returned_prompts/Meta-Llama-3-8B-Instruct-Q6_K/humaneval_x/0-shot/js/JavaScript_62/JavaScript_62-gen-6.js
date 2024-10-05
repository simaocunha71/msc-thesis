Here is the solution to the problem:
```
const derivative = (xs) => {
  const n = xs.length;
  const result = new Array(n - 1);
  for (let i = 1; i < n; i++) {
    result[i - 1] = i * xs[i];
  }
  return result;
};
```
Here's an explanation of the solution:

* We create a new array `result` of length `n-1` to store the coefficients of the derivative.
* We iterate over the coefficients of the original polynomial, starting from the second coefficient (index 1).
* For each coefficient, we multiply it by its index (which represents the power of `x` in the original polynomial) and store the result in the corresponding index of the `result` array.
* Finally, we return the `result` array.

This solution works because the derivative of a polynomial `p(x) = a0 + a1*x + a2*x^2 + ... + an*x^n` is `p'(x) = a1 + 2*a2*x + 3*a3*x^2 + ... + n*an*x^(n-1)`. By multiplying each coefficient by its index, we effectively calculate the derivative of the polynomial.

You can test this function with the examples provided in the problem statement:
```
console.log(derivative([3, 1, 2, 4, 5])); // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])); // [2, 6]
```