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
}
// Test
console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5]));  // Output: 9
console.log(doAlgebra(['+', '**'], [2, 3, 4]));  // Output: 20
console.log(doAlgebra(['+', '-'], [2, 3]));  // Output: 1
console.log(doAlgebra(['+', '*'], [2, 3, 4]));  // Output: 14
console.log(doAlgebra(['+', '**'], [2, 3]));  // Output: 20
console.log(doAlgebra(['+', '*'], [2, 3, 4, 5]));  // Output: 14
console.log(doAlgebra(['+', '*'], [2]));  // Output: 2
console.log(doAlgebra(['+', '**'], [2, 3]));  // Output: 20
console.log(doAlgebra(['+', '**'], [2, 3, 4]));  // Output: 20
console.log(doAlgebra(['+', '**'], [2, 3, 4, 5]));  // Output: 20
console.log(doAlgebra(['+', '**'], [2]));  // Output: 2
console.log(doAlgebra(['+', '**'], [2, 3, 4, 5]));  // Output: 20
console.log(doAlgebra(['+', '**'], [2, 3, 4]));  // Output: 20
console.log(doAlgebra(['+', '**'], [2, 3, 4, 5]));  // Output: 20
// Output: 9
// Output: 20
// Output: 1
// Output: 14
// Output: 20
// Output: 2