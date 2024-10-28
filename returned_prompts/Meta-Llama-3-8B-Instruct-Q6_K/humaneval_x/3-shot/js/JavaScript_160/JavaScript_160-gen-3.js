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
//Test
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
console.log(doAlgebra(operator, operand)) // Output: 9
//Test
operator = ['+', '**', '-']
operand = [2, 3, 4]
console.log(doAlgebra(operator, operand)) // Output: 23
//Test
operator = ['+', '*']
operand = [2, 3, 4, 5]
console.log(doAlgebra(operator, operand)) // Output: 14
//Test
operator = ['+', '*']
operand = [2, 3]
console.log(doAlgebra(operator, operand)) // Output: 8
//Test
operator = ['+', '*']
operand = [2]
console.log(doAlgebra(operator, operand)) // Output: 2
//Test
operator = ['+', '*']
operand = []
console.log(doAlgebra(operator, operand)) // Output: NaN
//Test
operator = []
operand = [2, 3]
console.log(doAlgebra(operator, operand)) // Output: 2
//Test
operator = ['+', '*']
operand = [2, 3, 4, 5, 6]
console.log(doAlgebra(operator, operand)) // Output: NaN
//Test
operator = ['+', '*']
operand = [2, 3, 4]
console.log(doAlgebra(operator, operand)) // Output: 14
//Test
operator = ['+', '*']
operand = [2, 3, 4, 5, 6, 7]
console.log(doAlgebra(operator, operand)) // Output: NaN
//Test
operator = ['+', '*']
operand = [2, 3, 4, 5, 6, 7, 8]
console.log(do