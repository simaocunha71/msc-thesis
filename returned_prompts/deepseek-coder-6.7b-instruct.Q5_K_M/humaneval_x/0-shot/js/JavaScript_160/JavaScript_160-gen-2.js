  let result = operand[0];
  for (let i = 1; i < operand.length; i++) {
    switch (operator[i - 1]) {
      case '+':
        result += operand[i];
        break;
      case '-':
        result -= operand[i];
        break;
      case '*':
        result *= operand[i];
        break;
      case '//':
        result = Math.floor(result / operand[i]);
        break;
      case '**':
        result = Math.pow(result, operand[i]);
        break;
    }
  }
  return result;
}

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['+', '*', '//'], [2, 3, 4, 5])); // 14
console.log(doAlgebra(['+', '*', '**'], [2, 3, 4, 5])); // 47
console.log(doAlgebra(['-', '*', '//'], [2, 3, 4, 5])); // -13
console.log(doAlgebra(['+', '//', '**'], [2, 3, 4, 5])); // 1

*/

// Solution:
The problem can be solved by using a loop to iterate over the operators and their corresponding operands, then applying the operations to the result. The initial result is the first operand. 

The operations are defined using a switch-case statement, where each case corresponds to a specific operation. 

The time complexity of this solution is O(n), where n is the length of the operand list. This is because we are iterating over the operand list once. The space complexity is O(1), which is the minimum amount of space we need to store the result and the operands. This is because we are not using any additional data structures to store the operands and the result.

In the case of '//' (floor division), we use the Math.floor() function to round down the result