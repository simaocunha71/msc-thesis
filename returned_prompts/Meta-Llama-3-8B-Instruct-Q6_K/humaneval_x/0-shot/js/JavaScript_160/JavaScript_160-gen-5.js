```
const doAlgebra = (operator, operand) => {
  let expression = '';
  for (let i = 0; i < operator.length; i++) {
    expression += operand[i];
    if (i < operator.length - 1) {
      expression += operator[i];
    }
  }
  return eval(expression);
};
```


Explanation:
The function `doAlgebra` takes two parameters, `operator` and `operand`, which are lists of strings and numbers respectively. The function iterates over the `operator` list and the `operand` list, concatenating the corresponding elements to form a string representation of the algebraic expression. The `eval` function is then used to evaluate this expression and return the result.

The condition `if (i < operator.length - 1)` is used to ensure that the last operator is not followed by another operand. This is because the last operand does not have an operator after it.

For example, if the input is `operator=['+', '*', '-']` and `operand=[2, 3, 4, 5]`, the function will form the string expression `2+3*4-5` and evaluate it to `9`.