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
        break;
    }
  }
  return result;
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['//', '*', '+'], [2, 3, 4, 5])); // 6
console.log(doAlgebra(['**', '*', '+'], [2, 3, 4, 5])); // 102

*/







































































































































































































































