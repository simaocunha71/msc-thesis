  let result = 0;
  for (let i = 0; i < operator.length; i++) {
    if (operator[i] === '+') {
      result = result + operand[i];
    } else if (operator[i] === '-') {
      result = result - operand[i];
    } else if (operator[i] === '*') {
      result = result * operand[i];
    } else if (operator[i] === '//') {
      result = result / operand[i];
    } else if (operator[i] === '**') {
      result = Math.pow(result, operand[i]);
    }
  }
  return result;

};

let operator = ['+', '-', '*'];
let operand = [1, 2, 3];
console.log(doAlgebra(operator, operand));
