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
      case '//' :
        result = Math.floor(result / num);
        break;
      case '**':
        result = Math.pow(result, num);
        break;
    }
  }
  return result;
};
```


Explanation:

1. Initialize the result with the first element of the operand list.
2. Iterate through the operator list. For each operator, use the corresponding element from the operand list.
3. Use a switch statement to apply the operation to the result. The operations are:
   - Addition: `result += num`
   - Subtraction: `result -= num`
   - Multiplication: `result *= num`
   - Floor division: `result = Math.floor(result / num)`
   - Exponentiation: `result = Math.pow(result, num)`
4. Return the final result.