Here is the solution to the problem:
```
const stringSequence = (n) => {
  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i + ' ';
  }
  return result.trim(); // remove trailing space
};
```
Here's an explanation of the code:

* We initialize an empty string `result` that will store the sequence of numbers.
* We use a `for` loop to iterate from 0 to `n` inclusive.
* Inside the loop, we concatenate each number `i` to the `result` string followed by a space using the `+` operator.
* After the loop, we use the `trim()` method to remove the trailing space from the `result` string.
* Finally, we return the `result` string.

You can test the function with different inputs, such as `stringSequence(0)` or `stringSequence(5)`, to see the expected output. For example, `stringSequence(0)` should return the string `'0'`, and `stringSequence(5)` should return the string `'0 1 2 3 4 5'`.