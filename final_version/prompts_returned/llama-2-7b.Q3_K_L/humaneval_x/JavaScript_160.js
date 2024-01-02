/*
  Given two lists operator, and operand. The first list has basic algebra operations, and 
  the second list is a list of integers. Use the two given lists to build the algebric 
  expression and return the evaluation of this expression.

  The basic algebra operations:
  Addition ( + ) 
  Subtraction ( - ) 
  Multiplication ( * ) 
  Floor division ( // ) 
  Exponentiation ( ** ) 

  Example:
  operator['+', '*', '-']
  array = [2, 3, 4, 5]
  result = 2 + 3 * 4 - 5
  => result = 9

  Note:
      The length of operator list is equal to the length of operand list minus one.
      Operand is a list of of non-negative integers.
      Operator list has at least one operator, and operand list has at least two operands.

  */
const doAlgebra = (operator, operand) => {
    let res;
    for(let i=0; i<Math.min(...operand.length); ++i){
        if (!isNaN(parseInt(operator[i]))) {
            const [num1, op, num2] = operator[i].split(/[\s-*/()]+/);
            let tempValue = parseInt(num1) * (op === '**') ? parseInt(num2) ** parseInt(num1) : parseFloat(num2) / parseFloat(num1);
            
            if (op === '+') {
                res += tempValue;
            } else if (op === '-'){
                res -= tempValue;
            } else if (op === '*') {
                res *= tempValue;
            } else {
                    res /= tempValue;
            }
        }
    }
   return Math.abs(res);
};