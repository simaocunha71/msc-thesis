Here is a JavaScript solution that calculates the Brazilian factorial:
```
const specialFactorial = (n) => {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
    if (i > 1) {
      for (let j = 2; j < i; j++) {
        result *= j;
      }
    }
  }
  return result;
};
```
Here's an explanation of the code:

* We initialize the `result` variable to 1.
* We loop from 1 to `n` (inclusive) using a `for` loop.
* For each iteration, we multiply the `result` by the current value of `i`.
* If `i` is greater than 1, we loop from 2 to `i-1` (inclusive) and multiply the `result` by each of these values. This is to calculate the factorial of `i-1`, `i-2`, ..., 1!.
* Finally, we return the calculated `result`.

For example, if we call `specialFactorial(4)`, the function will calculate the Brazilian factorial of 4 as follows:
```
result = 1 * 1! * 2! * 3! * 4! = 1 * 1 * 2 * 6 * 24 = 288
```
So, the output of `specialFactorial(4)` would be `288`.