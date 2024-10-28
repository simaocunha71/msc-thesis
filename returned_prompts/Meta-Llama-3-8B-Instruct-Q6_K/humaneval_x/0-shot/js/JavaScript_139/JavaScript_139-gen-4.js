```javascript
const specialFactorial = (n) => {
  if (n < 0) {
    throw new Error("Input must be a positive integer.");
  }
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i * specialFactorial(i - 1);
  }
  return result;
};
```


In this solution, we define the function `specialFactorial` that takes an integer `n` as input. We check if `n` is less than 0, and if so, we throw an error because the Brazilian factorial is only defined for positive integers.

We then initialize a variable `result` to 1 and use a for loop to calculate the Brazilian factorial. In each iteration, we multiply `result` by the product of the current number `i` and the Brazilian factorial of `i - 1`. This is done recursively until we reach `i = 1`.

Finally, we return the calculated Brazilian factorial.

Note: This solution uses recursion, which can be less efficient than an iterative solution for large values of `n`. However, for small to medium-sized inputs, this solution should work fine. For larger inputs, an iterative solution would be more efficient.