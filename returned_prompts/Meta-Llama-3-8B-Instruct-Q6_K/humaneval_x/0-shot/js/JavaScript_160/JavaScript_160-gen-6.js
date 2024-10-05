```
const doAlgebra = (operator, operand) => {
  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    const op = operator[i];
    const num = operand[i + 1];
    switch (op) {
      case '+':
        result += num;
        break;
      case '-':
        result -= num;
        break;
      case '*':
        result *= num;
        break;
      case '//' : // Floor division
        result = Math.floor(result / num);
        break;
      case '**':
        result = Math.pow(result, num);
        break;
      default:
        throw new Error(`Invalid operator: ${op}`);
    }
  }
  return result;
};
```



This function takes two lists as input: `operator` and `operand`. It uses the `operator` list to build an algebraic expression and evaluates it using the `operand` list. The function returns the result of the evaluation.

The `doAlgebra` function initializes the `result` variable with the first element of the `operand` list. Then, it iterates over the `operator` list and the `operand` list (starting from the second element of the `operand` list), using the current operator and operand to update the `result` variable. The switch statement is used to handle the different operators.

Note that the `//` operator is used for floor division, which is a built-in operator in Python but not in JavaScript. To achieve the same effect, we use the `Math.floor` function to divide the `result` by the operand and return the integer part of the result. The `**` operator is used for exponentiation, which is also a built-in operator in Python but not in JavaScript. To achieve the same effect, we use the `Math.pow` function to raise the `result` to the power of the operand. If an invalid operator is encountered, the function throws an error.

Finally, the function returns the `result` variable, which is the evaluation of the algebraic expression.