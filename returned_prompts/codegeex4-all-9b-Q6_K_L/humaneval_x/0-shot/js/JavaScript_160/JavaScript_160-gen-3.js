```javascript
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
        result **= operand[i + 1];
        break;
      default:
        throw new Error('Invalid operator');
    }
  }
  return result;
}
```
