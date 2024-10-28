  // solution here

};
















































*/ ———————————————————————————————————————————
function doAlgebra(operator, operand) {
  let i = 0;
  let result = operand[i];
  while (operator.length) {
    switch (operator.shift()) {
      case '+':
        result += operand.shift();
        break;
      case '-':
        result -= operand.shift();
        break;
      case '*':
        result *= operand.shift();
        break;
      case '//':
        result = Math.floor(result / operand.shift());
        break;
      case '**':
        result = Math.pow(result, operand.shift());
        break;
    }
  }
  return result;
}

doAlgebra(["+", "*", "-"], [1, 2, 3, 4, 5]);   // 9
doAlgebra(["+", "*", "-"], [1, 2, 3, 4]);     // 5
doAlgebra(["+", "*", "-"], [1, 2, 3]),       // 0
doAlgebra(["**", "**", "+"], [2, 3, 4]),     // 32
doAlgebra(["**", "**", "+"], [2, 3]),       // 0
doAlgebra(["**", "**", "+"], [2]),          // 0
doAlgebra(["**", "**", "+"], []),           // NaN
doAlgebra(["**"], [2]),                     // 4
doAlgebra(["**"], [2, 3]),                  // NaN
doAlgebra(["+"], [2]),                      // 2
doAlgebra(["+"], []),                       // NaN
doAlgebra(["**", "**"], [2]),               // 4
doAlgebra(["**", "**"], [2, 3]),            // NaN
doAlgebra