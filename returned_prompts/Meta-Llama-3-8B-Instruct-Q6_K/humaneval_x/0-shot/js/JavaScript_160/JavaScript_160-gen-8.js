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