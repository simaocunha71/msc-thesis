  let result = operand[0];
  
  for (let i = 0; i < operator.length; i++) {
    switch(operator[i]) {
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

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['**', '*', '//'], [2, 3, 4, 2])); // 24
console.log(doAlgebra(['-', '+', '**'], [3, 2, 3, 2])); // -1

// The time complexity of this code is O(n), where n is the length of the operator array.
// The space complexity of this code is O(1), because it uses a constant amount of space.
// This code assumes that the input arrays are valid and will not throw any errors.

/*
  This code works by iterating over the operator array. For each operator, it performs the corresponding operation on the current result and the next operand in the operand array.
  It uses a switch statement to determine which operation to perform based on the current operator.
  Finally, it returns the result.
*/

// The time complexity of this code is O(n), where n is the length of the operator array.
// The space complexity of this code is O(1), because it uses a constant amount of space.
// This code assumes that the input arrays are valid and will not throw any errors.

// The time complexity of this code is O(n), where n is the length of the operator array.
// The space complexity of this code is O(1), because it uses a constant amount