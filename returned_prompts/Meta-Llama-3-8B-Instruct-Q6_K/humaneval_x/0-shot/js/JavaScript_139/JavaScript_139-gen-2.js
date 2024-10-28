```
const specialFactorial = (n) => {
  if (n <= 0) {
    throw new Error("Input must be a positive integer");
  }
  let result = 1;
  for (let i = 1; i <= n; i++) {
    let factorial = 1;
    for (let j = 1; j <= i; j++) {
      factorial *= j;
    }
    result *= factorial;
  }
  return result;
};
```


Explanation:
The function `specialFactorial` takes an integer `n` as input and returns the Brazilian factorial of `n`. It first checks if `n` is less than or equal to 0, and if so, it throws an error.

Then, it initializes a variable `result` to 1. It then loops through the numbers from 1 to `n` using the outer loop, and for each number `i`, it calculates the factorial of `i` using the inner loop. The factorial of `i` is calculated by multiplying all the numbers from 1 to `i`.

The result of the factorial calculation for each `i` is multiplied with the current `result`. Finally, the function returns the `result`, which is the Brazilian factorial of `n`.