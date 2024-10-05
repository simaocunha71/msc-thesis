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
    }
  }

  return result;
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5]));  // Output: 9

// Explanation:
// 2 + 3 * 4 - 5 = 2 + 12 - 5 = 14 - 5 = 9.
// Therefore, the function returns 9.

*/

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
        result = Math.pow(result, operand[i + 1]);
        break;
    }
  }

  return result;
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // Output: 9

// Explanation:
// 2 + 3 * 4 - 5 = 2 + 12 - 5 = 14 - 5 = 9.