To solve this problem, we can follow these steps:

1. Initialize a variable, `result`, to 1. This will store the final result.
2. Iterate `n` times. For each iteration, multiply `result` by 2 and take the modulo `p`. Store the result back in `result`.
3. Return the final value of `result`.

Here's the JavaScript code that follows these steps:

```javascript
const modp = (n, p) => {
  let result = 1;
  for (let i = 0; i < n; i++) {
    result = (result * 2) % p;
  }
  return result;
};
```

This code defines a function called `modp` that takes two parameters: `n` and `p`. It initializes a variable `result` to 1. Then, it enters a loop that iterates `n` times. In each iteration, it multiplies the current value of `result` by 2 and takes the modulo `p`. Finally, it returns the result.

You can use this function to calculate 2^n modulo p. For example, calling `modp(3, 5)` will return 3, `modp(1101, 101)` will return 2, `modp(0, 101)` will return 1, `modp(3, 11)` will return 8, and `modp(100, 101)` will return 1.

This solution handles the numerics correctly by taking the modulo `p` in each iteration, which ensures that the result never exceeds the maximum value of `p`.

The time complexity of this solution is O(n), where n is the value of the first parameter. This means that the runtime of the function grows linearly with the value of `n`.

Overall, this solution provides an efficient and accurate way to calculate 2^n modulo p in JavaScript.

*/

Ans:
The provided code defines a JavaScript function called `modp` that takes two parameters: `n` and `p`. It calculates 2 raised to the power of `n` modulo `p`. Here's a breakdown