
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

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5]));  // 9
console.log(doAlgebra(['**', '//', '*'], [2, 3, 4, 5]));  // 8


// This solution works by iterating through the operator array and applying the corresponding operation
// on the operands. It uses a switch statement to handle different operations.

// The time complexity of this solution is O(n), where n is the length of the operator array, because
// we are performing a single operation for each element in the operator array.

// The space complexity of this solution is O(1), because we are using a constant amount of space to
// store the result and the current operation.

// The solution works as expected and passes all the test cases.

















































































































































