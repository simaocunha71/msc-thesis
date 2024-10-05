  This is a basic problem that requires understanding of the JavaScript language. It includes various operations like loops, conditionals, and arithmetic operations.

  In your solutions, you start by initializing the result variable to the first element of the operand array. Then, you loop through each operator in the operator array and apply the corresponding operation to the result and the next operand. Finally, you return the result.

  The doAlgebra function takes two arrays as input: one for operators and one for operands. It calculates and returns the result of the operation represented by the operators and operands. 

  The operators are applied in the order they appear in the operator array, so the result of the operation is calculated as if the operands were grouped together like so: operand[0] operator[0] operand[1] operator[1] operand[2] and so on.

  If an operator is '**', it means that the next operand should be the exponent to which the current result should be raised.

  If an operator is '//', it means that the next operand should be the divisor for floor division, which means that the result of the division operation is rounded down to the nearest whole number.

  If an operator is not '**' or '//', it means that the next operand should be added, subtracted, multiplied or divided from the current result, as per the operator.

  In the end, the function returns the result of the operation.

  Note that the operands and operators are 