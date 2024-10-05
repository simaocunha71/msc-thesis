  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    let op = operator[i];
    let operand1 = operand[i];
    let operand2 = operand[i + 1];
    switch (op) {
      case '+':
        result += operand2;
        break;
      case '-':
        result -= operand2;
        break;
      case '*':
        result *= operand2;
        break;
      case '//':
        result = Math.floor(result / operand2);
        break;
      case '**':
        result = Math.pow(result, operand2);
        break;
    }
  }
  return result;
}
// Example usage:
let operator = ['+', '*', '-'];
let operand = [2, 3, 4, 5];
console.log(doAlgebra(operator, operand)); // Output: 9
// Explanation: 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
// The operator list has three operators (+, *, -), and the operand list has four operands (2, 3, 4, 5).
// The function evaluates the expression as 2 + 3 * 4 - 5 and returns the result 9.