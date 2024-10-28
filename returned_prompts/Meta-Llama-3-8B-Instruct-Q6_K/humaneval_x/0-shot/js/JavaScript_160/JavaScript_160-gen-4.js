```
const doAlgebra = (operator, operand) => {
  if (operator.length !== operand.length - 1) {
    throw new Error('Invalid operator or operand');
  }
  if (operand.length < 2) {
    throw new Error('Invalid operand');
  }
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
      default:
        throw new Error('Invalid operator');
    }
  }
  return result;
};
```

This function first checks if the operator list and operand list have the correct length. It then initializes the result with the first operand. It then loops through the operator list, performing the corresponding operation on the result and the next operand. Finally, it returns the result.