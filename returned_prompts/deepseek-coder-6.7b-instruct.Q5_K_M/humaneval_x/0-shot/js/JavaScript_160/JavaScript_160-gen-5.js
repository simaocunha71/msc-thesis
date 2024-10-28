  let result = operand[0];
  
  for(let i = 0; i < operator.length; i++){
    switch(operator[i]){
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

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // Expected output: 9
console.log(doAlgebra(['**', '//', '*'], [2, 3, 4, 5])); // Expected output: 6


This function starts by initializing the result to the first element of the operand array. Then it iterates through each element in the operator array, applying the corresponding operation to the next element in the operand array and updating the result. The function returns the final result after all operations have been applied.

*/







































































































































































































