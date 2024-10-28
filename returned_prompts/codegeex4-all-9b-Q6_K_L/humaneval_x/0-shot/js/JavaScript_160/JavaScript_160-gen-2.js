```javascript
const doAlgebra = (operator, operand) => {
  return operator.reduce((prev, curr, i) => {
    switch (curr) {
      case '+':
        return prev + operand[i];
      case '-':
        return prev - operand[i];
      case '*':
        return prev * operand[i];
      case '//':
        return Math.floor(prev / operand[i]);
      case '**':
        return prev ** operand[i];
      default:
        return prev;
    }
  }, operand[0]);
};
```
