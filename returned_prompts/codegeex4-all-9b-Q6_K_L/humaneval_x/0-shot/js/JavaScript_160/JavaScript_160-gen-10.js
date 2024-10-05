To solve the problem, we need to iterate through the operator list and apply the corresponding operation to the operand list. We'll start by initializing a variable to store the result of the expression. Then, for each operator in the operator list, we'll get the corresponding operands, apply the operation, and update the result. Finally, we'll return the result.

Here's the complete solution:

```javascript
const doAlgebra = (operator, operand) => {
  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    const currentOperator = operator[i];
    const currentOperand = operand[i + 1];
    switch (currentOperator) {
      case '+':
        result += currentOperand;
        break;
      case '-':
        result -= currentOperand;
        break;
      case '*':
        result *= currentOperand;
        break;
      case '//':
        result = Math.floor(result / currentOperand);
        break;
      case '**':
        result **= currentOperand;
        break;
    }
  }
  return result;
};
```

This solution iterates through the operator list and applies the corresponding operation to the operand list. It uses a switch statement to handle each operator and updates the result accordingly. The final result is returned at the end of the function.