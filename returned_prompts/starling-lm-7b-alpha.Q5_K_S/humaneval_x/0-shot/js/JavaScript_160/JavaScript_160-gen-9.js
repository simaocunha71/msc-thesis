    let result = operand[0];
    for (let i = 1; i < operand.length; i++) {
      if (operator[i - 1] === "+") {
        result += operand[i];
      } else if (operator[i - 1] === "-") {
        result -= operand[i];
      } else if (operator[i - 1] === "*") {
        result *= operand[i];
      } else if (operator[i - 1] === "//") {
        result = Math.floor(result / operand[i]);
      } else if (operator[i - 1] === "**") {
        result = Math.pow(result, operand[i]);
      }
    }
    return result;
  };










/*
Given two lists operator, and operand. The first list has basic algebra operations, and 
the second list is a list of integers. Use the two given lists to build the algebric 
expression and return the evaluation of this expression.

The basic algebra operations:
Addition (+)
Subtraction (-)
Multiplication (*)
Floor division (//)
Exponentiation (**).

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





































*/

















































































