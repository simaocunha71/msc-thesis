```javascript
const doAlgebra = (operator, operand) => {
  if (operator.length === 0) {
    return operand[0];
  }
  const op = operator.shift();
  const left = doAlgebra(operator, operand);
  const right = operand.shift();
  if (op === '+') {
    return left + right;
  }
  if (op === '-') {
    return left - right;
  }
  if (op === '*') {
    return left * right;
  }
  if (op === '//') {
    return Math.floor(left / right);
  }
  if (op === '**') {
    return left ** right;
  }
};
```
