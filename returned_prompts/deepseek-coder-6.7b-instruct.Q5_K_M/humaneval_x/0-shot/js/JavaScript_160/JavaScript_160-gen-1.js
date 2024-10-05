
  // initialize result as the first operand
  let result = operand[0];

  // iterate over operator and operands
  for (let i = 0; i < operator.length; i++) {
    switch (operator[i]) {
      case '+':
        // add next operand to result
        result += operand[i + 1];
        break;
      case '-':
        // subtract next operand from result
        result -= operand[i + 1];
        break;
      case '*':
        // multiply next operand with result
        result *= operand[i + 1];
        break;
      case '//':
        // divide result by next operand
        result = Math.floor(result / operand[i + 1]);
        break;
      case '**':
        // raise result to the power of next operand
        result = Math.pow(result, operand[i + 1]);
        break;
    }
  }

  // return final result
  return result;
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['**', '//', '*'], [2, 3, 4, 5])); // 10

/*
  The doAlgebra function iterates over the operator array and the operand array. 
  It starts with the first operand and applies each operation in sequence to it. 
  The result of each operation is then used as the input for the next operation in the operand array. 
  This continues until all operations have been applied. The final result is then returned.
*/


*/

// this function is a simple implementation of a basic calculator that can handle addition, subtraction, multiplication, division and exponentiation.
// it takes two arguments: an array of operators and an array of operands.
// it returns the result of the calculated expression.

/*
  The function starts by initializing the result as the first operand in the operand array.
  It then loops over the operator array and the operand array.
  For each operator, it applies the corresponding operation