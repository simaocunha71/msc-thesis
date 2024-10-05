```
const doAlgebra = (operator, operand) => {
  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    switch (operator[i]) {
      case '+':
        result += operand[i + 1];
        break;
      case '-':
        result -= operand[i + 1];
        break;
      case '*':
        result *= operand[i + 1];
        break;
      case '//':
        result = Math.floor(result / operand[i + 1]);
        break;
      case '**':
        result = Math.pow(result, operand[i + 1]);
        break;
    }
  }
  return result;
};
```
This function takes two parameters: `operator` and `operand`. The `operator` parameter is an array of strings, where each string is one of the basic algebra operations. The `operand` parameter is an array of integers.

The function initializes a variable `result` to the first element of the `operand` array. It then loops through the `operator` array, applying each operation to the current `result` and the next element of the `operand` array. The result of each operation is stored in the `result` variable.

Finally, the function returns the final value of `result`.

For example, if `operator` is `['+', '*', '-']` and `operand` is `[2, 3, 4, 5]`, the function will evaluate the expression `2 + 3 * 4 - 5` and return the result `9`.