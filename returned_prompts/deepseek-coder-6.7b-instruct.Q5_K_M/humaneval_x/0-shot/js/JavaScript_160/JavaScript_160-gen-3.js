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

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['**', '//', '*'], [2, 3, 4, 5])); // 6
console.log(doAlgebra(['-', '+'], [24, 13, -2])); // 11

module.exports = doAlgebra;

// Time Complexity: O(n)
// Space Complexity: O(1)
// Where n is the length of the operator array.
